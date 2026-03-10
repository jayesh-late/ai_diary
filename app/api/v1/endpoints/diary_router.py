from datetime import date
from app.schemas.diary_schema import DiaryEntryCreate,DiaryEntryResponse
from fastapi import APIRouter,Query,HTTPException,status
from app.core.deps import DBSession, UserSession
from app.services.diary_service import DiaryService


router = APIRouter()


@router.post("/create",response_model=DiaryEntryResponse)
async def create_diary_entry(data:DiaryEntryCreate,db:DBSession,current_user:UserSession):
    user_id = 1
    return DiaryService.create_entry(
        db=db,
        user_id=current_user.id,
        data=data
    )

@router.get("/entries")
async def get_diary_entries(
        db:DBSession,
        current_user:UserSession,
        skip:int = Query(0, ge=0),
        limit:int = Query(10, le=100),
        start_date:date |None=None,
        end_date:date |None=None,

):
    user_id = current_user.id
    return DiaryService.get_entries(
        db=db,
        user_id=user_id,
        skip=skip,
        limit=limit,
        start_date=start_date,
        end_date=end_date
    )

@router.get("/entry/{entry_id}")
async def get_entry_by_id(db:DBSession,current_user:UserSession,entry_id:int):
    return DiaryService.get_entry_by_id(
        db=db,
        entry_id=entry_id,
        user_id = current_user.id
    )


@router.put("/update/entry/{entry_id}")
async def update_diary_entry(
        db:DBSession,
        current_user:UserSession,
        entry_id :int,
        data:DiaryEntryCreate
):
    return DiaryService.update_entry(
        db=db,
        user_id = current_user.id,
        entry_id=entry_id,
        data=data,

    )


@router.delete("/delete/entry/{entry_id}")
async def delete_diary_entry(
    db: DBSession,
    current_user: UserSession,
    entry_id: int
):
    return DiaryService.delete_entry(
        db=db,
        user_id=current_user.id,
        entry_id=entry_id
    )