# server/services/ai_service.py
from google.generativeai import GenerativeModel

class AIService:
    def __init__(self):
        self.model = GenerativeModel('gemini-pro')
    
    async def generate_description(self, prompt: str):
        response = self.model.generate_content(
            f"Explain this in simple terms: {prompt}"
        )
        return response.text
