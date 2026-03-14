from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional,List

class DiaryEntryCreate(BaseModel):
    date : date
    task_completed :str
    hour_studied :int
    mood : Optional[str] = None
    notes : Optional[str] = None

class DiaryEntryResponse(BaseModel):
    id : int
    date: date
    task_completed: str
    hour_studied: int
    mood: Optional[str]
    notes: Optional[str]

    model_config = ConfigDict(
        from_attributes= True
    )

class PaginatedDiaryEntryResponse(BaseModel):
    items : List[DiaryEntryResponse]
    total_entries : int
    page:int
    limit:int

    model_config = ConfigDict(
        from_attributes= True
    )
