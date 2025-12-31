from fastapi import FastAPI
from app.api.v1.health import router as HealthRouter
from app.api.v1.generate import router as GenerateRouter
app=FastAPI(title="GenAI FastAPI 30 Days")

app.include_router(HealthRouter,prefix="/api/v1")
app.include_router(GenerateRouter,prefix="/api/v1")
