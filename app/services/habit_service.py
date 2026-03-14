from app.repositories.habit_repository import HabitRepository
from sqlalchemy.orm import Session
from app.schemas.habit_schema import HabitCreate
from app.core.exceptions import HabitNotFoundException,InvalidCredentialsException
class HabitService:

    @staticmethod
    def create_habit(db:Session,user_id:int,data:HabitCreate):
        habit = HabitRepository.create_habit(
            db=db,
            user_id=user_id,
            data=data
        )
        if not habit:
            raise HabitNotFoundException()

        if habit.user_id != user_id:
            raise InvalidCredentialsException()

        return habit

    @staticmethod
    def list_habit(
            db:Session,
            user_id:int,
            page:int,
            limit:int
    ):
        offset = (page - 1) * limit
        habits = HabitRepository.get_user_habit(
            db=db,
            user_id=user_id,
            offset= offset,
            page=page,
            limit=limit
        )
        if not habits:
            raise HabitNotFoundException()


        for habit in habits:
            if habit.user_id != user_id:
                raise InvalidCredentialsException()

        total_habits = HabitRepository.count_user_habits(
            db=db,
            user_id=user_id
        )
        return {
            "items":habits,
            "total":total_habits,
            "page":page,
            "limit":limit
        }

    @staticmethod
    def get_habit(db:Session,user_id:int,habit_id:int):
        habit = HabitRepository.get_habit(
            db=db,
            habit_id=habit_id,
        )
        if not habit:
            raise HabitNotFoundException
        if habit.user_id != user_id:
            raise InvalidCredentialsException()

        return habit

    @staticmethod
    def complete_habit(db:Session,habit_id:int,date,user_id:int):
        habit = HabitRepository.get_habit(
            db=db,
            habit_id=habit_id
        )
        if not habit:
            raise HabitNotFoundException

        if habit.user_id != user_id:
            raise InvalidCredentialsException()

        return HabitRepository.log_completion(
            db=db,
            habit_id=habit_id,
            date=date
        )

