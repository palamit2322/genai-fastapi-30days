from app.models.prompt import PromptRequest
from app.core.dependencies import get_llm_service_v2
from app.services.llm_Service import LLMService
from fastapi import Depends,HTTPException,status,APIRouter
from app.core.exceptions import LLMServiceError

router=APIRouter()

@router.post("/generate")
async def generate_text(request:PromptRequest,llmService:LLMService=Depends(get_llm_service_v2)):
    if not request.prompt.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Prompt cannot be empty"
        )
    try:
        result=await llmService.generate(request.prompt)
        return {
            "version":"v2",
            "response":result
        }
    except LLMServiceError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))

    
