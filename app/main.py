from fastapi import FastAPI
from app.api.v1.health import router as HealthRouter
from app.api.v1.generate import router as GenerateRouter
from app.core.logging import setup_logging
from app.middleware.request_id import request_id_middleware
app=FastAPI(title="GenAI FastAPI 30 Days")
app.middleware("http")(request_id_middleware)
setup_logging()
app.include_router(HealthRouter,prefix="/api/v1")
app.include_router(GenerateRouter,prefix="/api/v1")
