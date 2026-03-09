from datetime import date
from app.schemas.diary_schema import DiaryEntryCreate,DiaryEntryResponse
from fastapi import APIRouter,Query
from app.core.deps import DBSession
from app.services.diary_service import DiaryService
from typing import List

router = APIRouter()

@router.post("/entry",response_model=DiaryEntryResponse)
async def create_diary_entry(data:DiaryEntryCreate,db:DBSession):
    user_id = 1
    return DiaryService.create_entry(
        db=db,
        user_id=user_id,
        data=data
    )

@router.get("/entries",response_model=List[DiaryEntryResponse])
async def get_diary_entries(
        db:DBSession,
        skip:int = Query(0, ge=0),
        limit:int = Query(10, le=100),
        start_date:date |None=None,
        end_date:date |None=None
):
    user_id = 1
    return DiaryService.get_entries(
        db=db,
        user_id=user_id,
        skip=skip,
        limit=limit,
        start_date=start_date,
        end_date=end_date
    )

@router.put("/update/{entry_id}")
async def update_diary_entry(
        db:DBSession,
        entry_id :int,
        data:DiaryEntryCreate
):
    return DiaryService.update_entry(
        db=db,
        entry_id=entry_id,
        data=data
    )

@router.delete("/delete/{entry_id}")
async def delete_diary_entry(db:DBSession,entry_id:int):
    return DiaryService.delete_entry(
        db=db,
        entry_id=entry_id
    )
