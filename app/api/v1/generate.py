from fastapi import APIRouter,Depends, HTTPException, status
from app.models.prompt import PromptRequest
from app.services.llm_Service import LLMService
from app.core.dependencies import get_llm_service
router=APIRouter()

@router.post("/generate")
def generate_text(request:PromptRequest, llm_service:LLMService=Depends(get_llm_service)):
    
    result=llm_service.generate(request.prompt)

    if not request.prompt.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="prompt cannot be empty"
        )
    return {
        "response": result
    }