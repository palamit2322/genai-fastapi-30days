from pydantic import BaseModel, Field

class LLMResponse(BaseModel):
    answer:str=Field(...,description="Main answer from LLM")
    confidence: float=Field(...,ge=0,le=1)