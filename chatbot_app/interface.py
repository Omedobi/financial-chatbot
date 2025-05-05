from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot_core.rag_engine import RAGChatbot

chatbot = RAGChatbot()
app = FastAPI()

class QueryInput(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Chatbot API is running"}

@app.post("/query")
def query_endpoint(input: QueryInput):
    try:
        response = chatbot.query(input.question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}