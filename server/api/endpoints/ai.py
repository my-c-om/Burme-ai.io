# server/api/endpoints/ai.py
from fastapi import APIRouter, Depends
from server.services.ai_service import AIService

router = APIRouter()
ai_service = AIService()

@router.post("/generate")
async def generate_text(prompt: str):
    return await ai_service.generate_description(prompt)
