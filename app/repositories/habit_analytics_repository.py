
from sqlalchemy.orm import Session
from app.db.models.habit_log_model import HabitLog
from app.db.models.habit_model import Habit

class HabitAnalyticsRepository:

    @staticmethod
    def get_habit_logs(
            db:Session,
            habit_id:int,
            offset:int,
            page:int,
            limit:int,
            user_id:int
    ):

        return (db.query(HabitLog)
                .join(Habit)
                .filter(HabitLog.habit_id == habit_id,
                        Habit.user_id == user_id)
                .order_by(HabitLog.completed.desc())
                .offset(offset)
                .limit(limit)
                )

    @staticmethod
    def count_habit_logs(
            db:Session,
            habit_id:int,
            user_id:int
    ):
        return (
            db.query(HabitLog)
            .join(Habit)
            .filter(HabitLog.habit_id == habit_id,
                    Habit.user_id ==user_id)
            .count()
        )


    @staticmethod
    def habit_log_list(db:Session,habit_id:int,user_id:int):
        return (db.query(HabitLog)
                .join(Habit)
                .filter(HabitLog.habit_id == habit_id,
                        Habit.user_id == user_id)
                .all())