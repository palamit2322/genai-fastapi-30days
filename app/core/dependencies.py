from app.services.llm_Service import LLMService
from app.core.prompts import SYSTEM_PROMPT,SYSTEM_PROMPT_V2
def get_llm_service()->LLMService:
    return LLMService(SYSTEM_PROMPT)

def get_llm_service_v2()-> LLMService:
    return LLMService(SYSTEM_PROMPT_V2)