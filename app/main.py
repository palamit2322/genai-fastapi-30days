from fastapi import FastAPI
from app.api.v1.health import router as HealthRouter

app=FastAPI(title="GenAI FastAPI 30 Days")

app.include_router(HealthRouter,prefix="/api/v1")
