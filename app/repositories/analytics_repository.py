from sqlalchemy.orm import Session
from app.db.models.diary_model import DailyEntry

class AnalyticsRepository:

    @staticmethod
    def get_user_entry_dates(db:Session,user_id:int):
        entries = (
            db.query(DailyEntry)
            .filter(DailyEntry.user_id == user_id)
            .order_by(DailyEntry.date.asc())
            .all()
        )
        return [entry.date for entry in entries]
