from pydantic import BaseModel
from datetime import date


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


class HabitLogCreate(BaseModel):
    date: date


class HabitLogResponse(BaseModel):

    id: int
    habit_id: int
    date: date
    completed: bool

    class Config:
        from_attributes = True