from fastapi import APIRouter
from app.core.deps import DBSession
from app.services.analytics_service import AnalyticsService


router = APIRouter()

@router.get("/streak")
async def get_streak(db:DBSession):
    user_id = 1
    return AnalyticsService.calculate_streak(
        db=db,
        user_id=user_id
    )