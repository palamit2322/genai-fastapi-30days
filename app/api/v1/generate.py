from fastapi import APIRouter,Depends, HTTPException, status
from app.models.prompt import PromptRequest
from app.services.llm_Service import LLMService
from app.core.dependencies import get_llm_service
from app.core.exceptions import LLMServiceError
from app.schemas.llm_response import LLMResponse
router=APIRouter()

@router.post("/generate")
async def generate_text(request:PromptRequest, llm_service:LLMService=Depends(get_llm_service)):
    
    if not request.prompt.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="prompt cannot be empty"
        )
    try:
        result= await llm_service.generate(request.prompt)
        return {
            "version":"v1",
            "response": result
        }
    except LLMServiceError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str())