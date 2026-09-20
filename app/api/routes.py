from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post('/chat')
async def chat(request: ChatRequest):
    from app.services.assistant import OpenAIAssistant
    assistant = OpenAIAssistant()
    response = await assistant.chat(request.message)
    return {'response': response}

@router.get('/health')
async def health():
    return {'status': 'ok'}