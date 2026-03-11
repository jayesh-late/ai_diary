from app.repositories.habit_repository import HabitRepository
from sqlalchemy.orm import Session
from app.schemas.habit_schema import HabitCreate
from fastapi import HTTPException,status
class HabitService:

    @staticmethod
    def create_habit(db:Session,user_id:int,data:HabitCreate):
        habit = HabitRepository.create_habit(
            db=db,
            user_id=user_id,
            data=data
        )
        if habit.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )

        return habit

    @staticmethod
    def list_habit(db:Session,user_id:int):
        habits = HabitRepository.get_user_habit(
            db=db,
            user_id=user_id
        )
        if not habits:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Habit Not Found"
            )


        for habit in habits:
            if habit.user_id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid Credentials"
                )

        return habits

    @staticmethod
    def get_habit(db:Session,user_id:int,habit_id:int):
        habit = HabitRepository.get_habit(
            db=db,
            habit_id=habit_id,
        )
        if not habit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Habit Not Found"
            )

        if habit.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )

        return habit

    @staticmethod
    def complete_habit(db:Session,habit_id:int,date,user_id:int):
        habit = HabitRepository.get_habit(
            db=db,
            habit_id=habit_id
        )
        if not habit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Habit Not Found"
            )

        if habit.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )

        return HabitRepository.log_completion(
            db=db,
            habit_id=habit_id,
            date=date
        )

