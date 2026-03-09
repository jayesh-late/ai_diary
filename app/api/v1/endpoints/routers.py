from fastapi import APIRouter
from app.api.v1.endpoints.diary import router as diary_router
from app.api.v1.endpoints.analytics import router as analytics_router

api_router = APIRouter()

api_router.include_router(
    diary_router,
    prefix="/diary",
    tags=["Diary"]
)
api_router.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)
