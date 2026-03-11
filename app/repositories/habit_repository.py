from app.db.models.habit_model import Habit
from app.db.models.habit_log_model import HabitLog
from sqlalchemy.orm import Session
from app.schemas.habit_schema import HabitCreate
class HabitRepository:

    @staticmethod
    def create_habit(db:Session,user_id:int,data:HabitCreate):
        habit = Habit(
            user_id = user_id,
            name = data.name,
            description = data.description
        )
        db.add(habit)
        db.commit()
        db.refresh(habit)

        return habit

    @staticmethod
    def get_user_habit(db:Session,user_id:int,skip:int=0,limit:int=10):
        return (
            db.query(Habit)
            .filter(Habit.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


    @staticmethod
    def get_habit(db:Session,habit_id:int):
        return db.query(Habit).filter(Habit.id == habit_id).first()


    @staticmethod
    def log_completion(db:Session,habit_id:int,date):
        log = HabitLog(
            habit_id = habit_id,
            date= date,
            completed= True
        )
        db.add(log)
        db.commit()
        db.refresh(log)

        return log