from fastapi import APIRouter,Depends
from app.models.prompt import PromptRequest
from app.services.llm_Service import LLMService
from app.core.dependencies import get_llm_service
router=APIRouter()

@router.post("/generate")
def generate_text(request:PromptRequest, llm_service:LLMService=Depends(get_llm_service)):
    
    result=llm_service.generate(request.prompt)
    return {
        "response": result
    }