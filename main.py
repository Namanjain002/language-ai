from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from ai.engine import get_validated_response
from ai.openai_client import OpenAIClient
from ai.validator import InvalidAIResponse
from session.state import ChatSession
from session.summary import context


app = FastAPI()

client = OpenAIClient()
session = ChatSession()


# -------------------------
# Request format
# -------------------------

class ChatRequest(BaseModel):
    message: str


# -------------------------
# Serve frontend
# -------------------------

@app.get("/")
def serve_frontend():
    return FileResponse("index.html")


# -------------------------
# Chat API
# -------------------------

@app.post("/api/chat")
def chat(request: ChatRequest):

    user_message = request.message.strip()

    if not user_message:
        return {
            "error": "Message cannot be empty"
        }

    try:
        response = get_validated_response(
            client,
            user_message
        )

        session.record(user_message, response)

        if response.corrected_text:
            context(response.corrected_text)
        context(response.reply)

        return {
            "has_error": response.has_error,
            "corrected_text": response.corrected_text,
            "reply": response.reply,
            "error_categories": response.error_categories
        }

    except InvalidAIResponse:
        return {
            "error": "AI returned an invalid response"
        }

