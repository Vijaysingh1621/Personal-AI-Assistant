

## 🤖 Personal AI Assistant using Gemini & FastAPI

This is a full-stack backend project that builds a **personal AI chatbot** using **Google Gemini Pro**, **FastAPI**, and **MongoDB** for chat history memory. Deployable on platforms like **Render**, and easily runnable locally using `uvicorn`.

---

### 📸 Demo

```
POST /chat/
{
  "user_input": "Hello, what's the weather like today?",
  "user_id": "vijay123"
}

Response:
{
  "response": "Hello! I don't have real-time weather info, but I can help with many other things. 😊"
}
```

---

### 🧠 Features

* ✅ Conversational memory stored per user in MongoDB.
* 🤝 Personalized chat using user IDs.
* 🧠 Gemini Pro (via LangChain) as the LLM backend.
* 🏃 FastAPI as the backend framework.
* ☁️ Ready for deployment on **Render** or similar.
* 📜 Clean `.env` usage for API and DB keys.

---

### 🚀 Tech Stack

| Technology        | Description                        |
| ----------------- | ---------------------------------- |
| FastAPI           | Web framework for building APIs    |
| LangChain         | Integration wrapper for Gemini API |
| Google Gemini Pro | LLM used for chat responses        |
| MongoDB           | Stores per-user chat history       |
| Uvicorn           | ASGI server to run FastAPI         |
| dotenv            | Loads secrets from `.env` file     |

---

### 📁 Project Structure

```
ai-chatbot-assist/
│
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not checked in)
├── README.md            # Project documentation
└── ...
```

---

### 📦 Installation & Setup

#### ✅ 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-chatbot-assist.git
cd ai-chatbot-assist
```

#### ✅ 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### ✅ 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🔐 .env Configuration

Create a `.env` file in the root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
MONGO_DB_URI=your_mongodb_atlas_uri
PORT=8000  # Optional: for local use
```

> 🌐 Gemini API docs: [https://ai.google.dev/gemini-api](https://ai.google.dev/gemini-api)
> ☁️ Get a free MongoDB URI from: [https://cloud.mongodb.com/](https://cloud.mongodb.com/)

---

### ▶️ Run Locally

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You can now test endpoints at:

```
http://localhost:8000/
http://localhost:8000/chat/
```

---

### 🧪 Test Chat Endpoint

Use tools like `curl`, Postman, or HTTPie.

Example `curl`:

```bash
curl -X POST http://localhost:8000/chat/ \
-H "Content-Type: application/json" \
-d '{"user_input": "Hi there!", "user_id": "user1"}'
```

---

### 🚀 Deploying on Render

1. Push your code to GitHub.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. Add environment variables in Render Dashboard:

   * `GOOGLE_API_KEY`
   * `MONGO_DB_URI`

Render will auto-detect and deploy your app!

---

### ✨ Credits

* [LangChain](https://www.langchain.com/)
* [Google Gemini API](https://ai.google.dev/)
* [MongoDB Atlas](https://cloud.mongodb.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Render Deployment Docs](https://render.com/docs)

---

### 📄 License

MIT License — feel free to use, modify, and share.

---

