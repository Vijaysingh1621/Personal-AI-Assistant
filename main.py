import os
from fastapi import FastAPI, Body
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient
import uvicorn

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
mongo_url = os.getenv("MONGO_DB_URI")

# Initialize MongoDB client
try:
    client = MongoClient(mongo_url)
    db = client["chat_memory"]  # Database name
    collection = db["conversations"]  # Collection name
    print("✅ Connected to MongoDB")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")

# Initialize FastAPI
app = FastAPI()

# Initialize Gemini AI
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=api_key,
    temperature=0.7
)

# Define request model
class ChatInput(BaseModel):
    user_input: str
    user_id: str  # Unique identifier for users

@app.get("/")
def home():
    return {"message": "Personal AI Assistant is running!"}

@app.post("/chat/")
def chat(chat_input: ChatInput = Body(...)):
    user_input = chat_input.user_input
    user_id = chat_input.user_id  # Get user_id from request

    if not user_input:
        return {"error": "No user input provided"}

    # Retrieve past conversation from MongoDB
    history_doc = collection.find_one({"user_id": user_id})
    chat_history = history_doc["messages"] if history_doc else []

    try:
        # Generate AI response
        prompt = f"Previous conversation: {chat_history}\nUser: {user_input}"
        response = llm.invoke(prompt)

        # Extract response text
        response_text = response.content if hasattr(response, 'content') else str(response)

        # Update conversation history in MongoDB
        chat_history.append({"user": user_input, "bot": response_text})
        collection.update_one(
            {"user_id": user_id},
            {"$set": {"messages": chat_history}},
            upsert=True
        )

        return {"response": response_text}
    except Exception as e:
        return {"error": str(e)}

# Run FastAPI on Render-compatible PORT
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render assigns PORT dynamically
    uvicorn.run(app, host="0.0.0.0", port=port)
