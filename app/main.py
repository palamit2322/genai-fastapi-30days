from fastapi import FastAPI
from app.core.logging import setup_logging
from app.middleware.request_id import request_id_middleware
from app.api.v1.routes import router as v1_router

app=FastAPI(title="GenAI FastAPI 30 Days")

app.middleware("http")(request_id_middleware)

setup_logging()

app.include_router(v1_router)
