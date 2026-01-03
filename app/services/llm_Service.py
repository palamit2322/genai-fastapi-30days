import asyncio
from  openai import OpenAI
from app.core.config import get_settings
class LLMService:

    def __init__(self):
        self.settings=get_settings()
        self.client=OpenAI(api_key=self.settings.OPENAI_API_KEY)

    async def generate(self,prompt:str)->str:
        #asyncio.sleep(5)
        response=self.client.chat.completions.create(
            model=self.settings.MODEL_NAME,
            messages=[
                {"role":"user","content":prompt}
            ],
            temperature=self.settings.TEMPERATURE

        )
        return (
            response.choices[0].message.content
        )
    