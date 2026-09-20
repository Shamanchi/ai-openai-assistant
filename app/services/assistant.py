import openai
from loguru import logger
from app.core.config import settings


class OpenAIAssistant:
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        self.temperature = settings.openai_temperature
        self.max_tokens = settings.max_tokens
    
    async def chat(self, message: str, functions: list = None) -> str:
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': message}
        ]
        
        kwargs = {
            'model': self.model,
            'messages': messages,
            'temperature': self.temperature,
            'max_tokens': self.max_tokens
        }
        
        if functions and settings.function_calling:
            kwargs['functions'] = functions
            kwargs['function_call'] = 'auto'
        
        response = await self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content
    
    async def close(self):
        await self.client.close()