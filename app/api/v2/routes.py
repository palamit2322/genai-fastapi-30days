from fastapi import APIRouter
from app.api.v2.generate import router as generate_router

router=APIRouter(prefix="/api/v2")
router.include_router(generate_router)