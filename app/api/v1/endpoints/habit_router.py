
from fastapi import APIRouter,Depends,Query
from app.core.deps import get_db,get_current_user
from app.schemas.habit_schema import HabitCreate,HabitResponse,HabitLogCreate,HabitLogResponse,PaginatedHabitResponse
from app.services.habit_service import HabitService
from typing import List,Annotated
from sqlalchemy.orm import Session
from app.db.models.user_model import User
DBSession = Annotated[Session,Depends(get_db)]
UserSession = Annotated[User,Depends(get_current_user)]
router = APIRouter()

@router.post("/create",response_model=HabitResponse)
async def create_habit(
        db:DBSession,
        current_user:UserSession,
        data:HabitCreate
):

    return HabitService.create_habit(
        db=db,
        user_id=current_user.id,
        data=data
    )

@router.get("/habits_list",response_model=PaginatedHabitResponse)
async def habit_list(
        db:DBSession,
        create_user:UserSession,
        page:int,
        limit:int = Query(default=10,ge=1,le=100)
    ):

    return HabitService.list_habit(
        db=db,
        user_id=create_user.id,
        page=page,
        limit=limit
    )

@router.get("/habit/{habit_id}")
async def get_habit(db:DBSession,
                    habit_id:int,
                    current_user:UserSession
    ):

    return HabitService.get_habit(
        db=db,
        habit_id = habit_id,
        user_id=current_user.id
    )

@router.post("/{habit_id}/complete",response_model=HabitLogResponse)
async def complete_habit(
        habit_id:int,
        data:HabitLogCreate,
        db:DBSession,
        current_user:UserSession
    ):

    return HabitService.complete_habit(
        db=db,
        habit_id=habit_id,
        date=data.date,
        user_id=current_user.id
    )
