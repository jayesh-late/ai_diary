from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import List

class HabitCreate(BaseModel):
    name: str
    description: str


class HabitResponse(BaseModel):

    id: int
    name: str
    description: str
    is_active: bool

    class Config:
        from_attributes = True

class PaginatedHabitResponse(BaseModel):
    items: List[HabitResponse]
    total: int
    page: int
    limit: int

    model_config = ConfigDict(
        from_attributes=True
    )


class HabitLogCreate(BaseModel):
    date: date


class HabitLogResponse(BaseModel):

    id: int
    habit_id: int
    date: date
    completed: bool

    model_config = ConfigDict(
        from_attributes=True
    )

class PaginatedHabitLogs(BaseModel):
    items : List[HabitLogResponse]
    total : int
    page : int
    limit : int

    model_config = ConfigDict(
        from_attributes= True
    )