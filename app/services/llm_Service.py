import asyncio
from app.core.config import get_settings
class LLMService:

    def __init__(self):
        self.settings=get_settings()

    async def generate(self,prompt:str)->str:
        asyncio.sleep(5)
        return (
            f"Model: {self.settings.MODEL_NAME}",
            f"Temperature: {self.settings.TEMPERATURE}",
            f"Prompt: {prompt}"
        )
    