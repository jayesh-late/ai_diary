from fastapi import APIRouter
from app.api.v1.endpoints.diary_router import router as diary_router
from app.api.v1.endpoints.auth_router import router as auth_router
from app.api.v1.endpoints.habit_router import router as habit_router
from app.api.v1.endpoints.social_auth_router import router as social_auth_router
from app.api.v1.endpoints.subscription_router import router as subscription_router
from app.api.v1.endpoints.habit_analytics_router import router as habit_analytics_router

api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    social_auth_router,
    prefix="/auth/social",
    tags=["Social Auth"]
)

api_router.include_router(
    subscription_router,
    prefix="/subscriptions",
    tags=["Subscriptions"]
)

api_router.include_router(
    diary_router,
    prefix="/diary",
    tags=["Diary"]
)

api_router.include_router(
    habit_router,
    prefix="/habit",
    tags=["Habit"]
)

api_router.include_router(
    habit_analytics_router,
    prefix="/habits",
    tags=["Habit Analytics"]
)

