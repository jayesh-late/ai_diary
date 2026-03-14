from fastapi import APIRouter,Depends,Query
from sqlalchemy.orm import Session
from app.db.models.user_model import User
from app.services.habit_analytcs_service import HabitAnalyticsService
from typing import Annotated
from app.core.deps import get_db,get_current_user
from app.schemas.habit_schema import PaginatedHabitLogs

DBSession = Annotated[Session,Depends(get_db)]
UserSession = Annotated[User,Depends(get_current_user)]

router = APIRouter()

@router.get("/{habit_id}/history",response_model=PaginatedHabitLogs)
async def habit_history(
        db:DBSession,
        current_user:UserSession,
        habit_id:int,
        page:int,
        limit:int = Query(default=20,ge=1,le=100)
):
    return HabitAnalyticsService.get_history(
        db=db,
        habit_id=habit_id,
        page=page,
        limit=limit,
        user_id=current_user.id
    )

@router.get("/{habit_id}/streak")
async def habit_streak(
        db:DBSession,
        habit_id:int,
        current_user:UserSession
):
    return HabitAnalyticsService.calculate_streak(
        db=db,
        habit_id=habit_id,
        user_id=current_user.id
    )

@router.get("/{habit_id}/analytics")
async def habit_analytics(
        db:DBSession,
        habit_id:int,
        current_user:UserSession
):
    return HabitAnalyticsService.completion_rate(
        db=db,
        habit_id=habit_id,
        user_id=current_user.id
    )