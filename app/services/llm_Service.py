import asyncio
from  openai import OpenAI
from app.core.config import get_settings
from app.core.prompts import SYSTEM_PROMPT
from app.core.exceptions import LLMServiceError
class LLMService:

    def __init__(self):
        self.settings=get_settings()
        self.client=OpenAI(api_key=self.settings.OPENAI_API_KEY)

    async def generate(self,user_prompt:str)->str:
        #asyncio.sleep(5)
        try:
            response=self.client.chat.completions.create(
                model=self.settings.MODEL_NAME,
                messages=[
                    {"role":"system","content":SYSTEM_PROMPT},
                    {"role":"user","content":user_prompt}
                ],
                temperature=self.settings.TEMPERATURE,
                timeout=10
            )
            if not response.choices:
                raise LLMServiceError("Empty response from LLM")
            
            return (
                response.choices[0].message.content
            )
        except Exception as e:
            LLMServiceError(str(e))



    