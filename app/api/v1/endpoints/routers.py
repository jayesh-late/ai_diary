from app.api.v1.endpoints.diary import router as diary_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    diary_router,
    prefix="/diary",
    tags=["Diary"]
)