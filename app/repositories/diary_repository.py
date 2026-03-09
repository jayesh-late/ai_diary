from sqlalchemy.orm import Session
from app.db.models.diary_model import DailyEntry
from app.schemas.diary_schema import DiaryEntryCreate
from datetime import date
class DiaryRepository:

    @staticmethod
    def create_entry(db:Session,user_id:int,data:DiaryEntryCreate):
        entry = DailyEntry(
            user_id = user_id,
            date = data.date,
            task_completed = data.task_completed,
            hour_studied = data.hour_studied,
            mood = data.mood,
            notes = data.notes,
    )
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    @staticmethod
    def get_entries(db:Session,user_id:int,
                    skip:int=0,limit:int=10,
                    start_date:date|None=None,end_date:date|None=None):
        query = db.query(DailyEntry).filter(DailyEntry.user_id == user_id)

        if start_date:
            query = query.filter(DailyEntry.date >= start_date)

        if end_date:
            query =query.filter(DailyEntry.date <= end_date)

        return (
            query
            .order_by(DailyEntry.date.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def update_entry(db:Session,entry_id:int,data:DiaryEntryCreate):
        entry = db.query(DailyEntry).filter(DailyEntry.id == entry_id).first()

        if not entry:
            return None

        entry.date = data.date
        entry.task_completed = data.task_completed
        entry.hour_studied = data.hour_studied
        entry.mood = data.mood
        entry.notes = data.notes

        db.commit()
        db.refresh(entry)
        return entry

    @staticmethod
    def delete_entry(db:Session,entry_id:int):
        entry = db.query(DailyEntry).filter(DailyEntry.id == entry_id).first()

        if not entry :
            return None

        db.delete(entry)
        db.commit()

        return entry