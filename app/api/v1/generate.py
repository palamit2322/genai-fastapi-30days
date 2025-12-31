from fastapi import APIRouter
from app.models.prompt import PromptRequest

router=APIRouter()

@router.post("/generate")
def generate_text(request:PromptRequest):
    return {
        "response": f"You said: {request.prompt}"
    }