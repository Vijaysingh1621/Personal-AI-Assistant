📌 Personal AI Assistant using FastAPI, Gemini AI, and MongoDB
🚀 Personal AI Assistant that remembers conversations and provides intelligent responses using Google Gemini API. Built with FastAPI, MongoDB, and LangChain, this AI assistant stores chat history in a database to maintain context across sessions.


📸 Demo
bash
Copy
Edit
POST /chat/
{
  "user_input": "Hello, what's the weather like today?",
  "user_id": "vijay123"
}

Response:
{
  "response": "Hello! I don't have real-time weather info, but I can help with many other things. 😊"
}
🧠 Features
✅ Conversational memory stored per user in MongoDB.

🤝 Personalized chat using user IDs.

🧠 Gemini Pro (via LangChain) as the LLM backend.

🏃 FastAPI as the backend framework.

☁️ Ready for deployment on Render or similar.

📜 Clean .env usage for API and DB keys.

🚀 Tech Stack
Technology	Description
FastAPI	Web framework for building APIs
LangChain	Integration wrapper for Gemini API
Google Gemini Pro	LLM used for chat responses
MongoDB	Stores per-user chat history
Uvicorn	ASGI server to run FastAPI
dotenv	Loads secrets from .env file

📁 Project Structure
bash
Copy
Edit
ai-chatbot-assist/
│
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not checked in)
├── README.md            # Project documentation
└── ...
📦 Installation & Setup
✅ 1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/ai-chatbot-assist.git
cd ai-chatbot-assist
✅ 2. Create and activate virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
✅ 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 .env Configuration
Create a .env file in the root:

env
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
MONGO_DB_URI=your_mongodb_atlas_uri
PORT=8000  # Optional: for local use
🌐 Gemini API docs: https://ai.google.dev/gemini-api
☁️ Get a free MongoDB URI from: https://cloud.mongodb.com/

▶️ Run Locally
bash
Copy
Edit
uvicorn main:app --reload --host 0.0.0.0 --port 8000
You can now test endpoints at:

bash
Copy
Edit
http://localhost:8000/
http://localhost:8000/chat/
🧪 Test Chat Endpoint
Use tools like curl, Postman, or HTTPie.

Example curl:

bash
Copy
Edit
curl -X POST http://localhost:8000/chat/ \
-H "Content-Type: application/json" \
-d '{"user_input": "Hi there!", "user_id": "user1"}'
🚀 Deploying on Render
Push your code to GitHub.

Create a new Web Service on Render.

Set Build Command: pip install -r requirements.txt

Set Start Command:

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port $PORT
Add environment variables in Render Dashboard:

GOOGLE_API_KEY

MONGO_DB_URI

Render will auto-detect and deploy your app!

🛠 Troubleshooting
Issue	Fix
429 quota exceeded	You're using Gemini's free tier limits. Wait or upgrade billing.
curl: URL malformed	Ensure JSON uses double quotes and valid syntax.
MongoError	Check your MONGO_DB_URI and DB permissions.
Port not open on Render	Ensure you bind to 0.0.0.0 and use the PORT env variable.

🧾 Example MongoDB Document
json
Copy
Edit
{
  "user_id": "vijay123",
  "messages": [
    {"user": "Hi", "bot": "Hello! How can I assist you today?"},
    {"user": "What's 2 + 2?", "bot": "It's 4."}
  ]
}
✨ Credits
LangChain

Google Gemini API

MongoDB Atlas

FastAPI

Render Deployment Docs

📄 License
MIT License — feel free to use, modify, and share.
