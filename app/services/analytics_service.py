from sqlalchemy.orm import Session
from app.repositories.analytics_repository import AnalyticsRepository
from datetime import timedelta

class AnalyticsService:

    @staticmethod
    def calculate_streak(db:Session,user_id:int):
        dates = AnalyticsRepository.get_user_entry_dates(
            db=db,
            user_id=user_id
        )

        if not dates:
            return {
                "Current Streak" : 0,
                "Longest Streak" : 0
            }

        longest = 1
        current = 1
        for i in range(len(dates)):
            if dates[i] == dates[i-1] + timedelta(days=1):
                current += 1
                longest =max(longest,current)
            else :
                current = 1

        return {
            "Current Streak": current,
            "Longest Streak" : longest
        }

