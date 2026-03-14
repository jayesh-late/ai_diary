from datetime import timedelta,date
from sqlalchemy.orm import Session

from app.api.v1.endpoints.habit_router import habit_list
from app.repositories.habit_analytics_repository import HabitAnalyticsRepository
from app.core.exceptions import HabitLogNotFoundException,HabitNotFoundException


class HabitAnalyticsService:

    @staticmethod
    def get_history(
            db:Session,
            habit_id:int,
            page:int,
            limit:int,
            user_id:int
    ):
        offset = (page -1)*limit

        logs = HabitAnalyticsRepository.get_habit_logs(
            db=db,
            habit_id=habit_id,
            offset= offset,
            page=page,
            limit=limit,
            user_id=user_id
        )
        if not logs :
            raise HabitLogNotFoundException()

        total = HabitAnalyticsRepository.count_habit_logs(
            db=db,
            habit_id=habit_id,
            user_id=user_id
        )
        return {
            "items":logs,
            "total":total,
            "page":page,
            "limit":limit
        }



    @staticmethod
    def calculate_streak(
            db:Session,
            habit_id:int,
            user_id:int
    ):
        logs = HabitAnalyticsRepository.habit_log_list(
            db=db,
            habit_id=habit_id,
            user_id=user_id
        )

        if not logs :
            return {"current_streak": 0,
                    "longest_streak":0}

        dates = sorted([log.date for log in logs])
        today = date.today()
        yesterday = today - timedelta(days=1)

        last_date = dates[-1]

        #===================#
        #  CURRENT STREAK   #
        #===================#


        if last_date < yesterday:
            current_streak = 0
        else:
            current_streak = 1

            for i in range(len(dates) - 1, 0, -1):

                if dates[i] - dates[i - 1] == timedelta(days=1):
                    current_streak += 1
                else:
                    break


        #==================#
        #  LONGEST STREAK  #
        #==================#
        temp_streak = 1
        longest_streak = 1

        for i in range(1,len(dates)):
            if dates[i] - dates[i - 1] == timedelta(days=1):
                temp_streak += 1
                longest_streak = max(longest_streak,temp_streak)

            else:
                temp_streak = 1

        return {
            "current_streak":current_streak,
            "longest_streak":longest_streak
        }

    @staticmethod
    def completion_rate(
            db:Session,
            habit_id:int,
            user_id:int
    ):
        logs = HabitAnalyticsRepository.habit_log_list(
            db=db,
            habit_id=habit_id,
            user_id=user_id
        )
        if not logs:
            return {"completion_rate":0}

        dates = sorted(log.date for log in logs)
        first_day = dates[0]
        last_date = dates[-1]

        total_days = (last_date - first_day).days + 1

        if total_days <= 0:
            return {"completion_rate": 0}

        completed_days = sum(1 for log in logs if log.completed)

        completion_rate = (completed_days / total_days) * 100

        return {
            "completion_rate": round(completion_rate,2),
            "completed_days":completed_days,
            "total_days":total_days
        }