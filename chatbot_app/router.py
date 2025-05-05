from fastapi import APIRouter, Request
from chatbot_app.interface import RAGChatbot

router = APIRouter()
chatbot = RAGChatbot()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        return {"error": "Query is required"}

    response = chatbot.query(query)
    return {"response": response}