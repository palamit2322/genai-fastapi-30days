import asyncio
import json
from  openai import OpenAI
from app.core.config import get_settings
from app.core.prompts import SYSTEM_PROMPT
from app.core.exceptions import LLMServiceError
from app.schemas.llm_response import LLMResponse
import logging

logger=logging.getLogger(__name__)
class LLMService:

    def __init__(self):
        self.settings=get_settings()
        self.client=OpenAI(api_key=self.settings.OPENAI_API_KEY)
        self.MAX_RETRY=3
        self.MAX_DELAY=1

    async def generate(self,user_prompt:str)->str:
        #asyncio.sleep(5)
        last_error = None
        for attempt in range(1,self.MAX_RETRY+1):
            try:
                logger.info("LLM call started....")
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
                    logger.warning("Empty response from LLM")
                    raise LLMServiceError("Empty response from LLM")
                logger.info("LLm call successful")
                return response.choices[0].message.content  
            except Exception as e:
              last_error=e
              print(f"Attempt {attempt} failed:{last_error}")
              if attempt< self.MAX_RETRY:
                  asyncio.sleep(self.MAX_DELAY)
              else:
                  logger.error("LLM call failed",exc_info=True)
                  raise LLMServiceError(f"LLM failed after {self.MAX_RETRY} attempts:str(e)")

                        
              
        



    