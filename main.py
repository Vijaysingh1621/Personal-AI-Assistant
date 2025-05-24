import os
from fastapi import FastAPI, Body
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient
from contextlib import asynccontextmanager
import uvicorn

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
mongo_url = os.getenv("MONGO_DB_URI")
port = int(os.getenv("PORT", 10000))  # Default to 10000 if PORT is not set

# Global shared resources (initialized in lifespan)
client = None
db = None
collection = None
llm = None

# FastAPI startup optimization
@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, db, collection, llm

    # Initialize MongoDB and LLM once on server start
    client = MongoClient(mongo_url)
    db = client["chat_memory"]
    collection = db["conversations"]

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # faster and cost-effective
        google_api_key=api_key,
        temperature=0.7
    )

    print("✅ AI model and DB initialized")
    yield
    # Optionally close resources here on shutdown

# Initialize FastAPI with lifespan handler
app = FastAPI(lifespan=lifespan)

# Pydantic input model
class ChatInput(BaseModel):
    user_input: str
    user_id: str

@app.get("/")
def home():
    return {"message": "🚀 Personal AI Assistant is running!"}

@app.post("/chat/")
def chat(chat_input: ChatInput = Body(...)):
    user_input = chat_input.user_input
    user_id = chat_input.user_id

    if not user_input:
        return {"error": "No user input provided"}

    # Retrieve past conversation from MongoDB
    history_doc = collection.find_one({"user_id": user_id})
    chat_history = history_doc["messages"] if history_doc else []

    try:
        # Build prompt with memory
        prompt = f"Previous conversation: {chat_history}\nUser: {user_input}"
        response = llm.invoke(prompt)

        # Extract response text
        response_text = response.content if hasattr(response, 'content') else str(response)

        # Save to MongoDB
        chat_history.append({"user": user_input, "bot": response_text})
        collection.update_one(
            {"user_id": user_id},
            {"$set": {"messages": chat_history}},
            upsert=True
        )

        return {"response": response_text}
    except Exception as e:
        return {"error": str(e)}

# Local run config
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
