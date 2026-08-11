import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def load_skill_prompt():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    skill_file = os.path.join(base_dir, "SKILL.md")
    if os.path.exists(skill_file):
        with open(skill_file, "r") as f:
            return f.read()
    return "You are a helpful AI chatbot assistant."

system_prompt = load_skill_prompt()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"status": "ok", "message": "Thermoplastic Road Markings API is running"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    chat = model.start_chat(history=[])
    chat.send_message(system_prompt)
    response = chat.send_message(request.message)
    return {"reply": response.text}

@app.get("/api/health")
async def health():
    return {"status": "ok"}