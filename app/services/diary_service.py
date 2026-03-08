from app.repositories.diary_repository import DiaryRepository
from sqlalchemy.orm import Session
from app.schemas.diary_schema import DiaryEntryCreate

class DiaryService:
    @staticmethod
    def create_entry(db:Session,user_id:int,data:DiaryEntryCreate):
        return DiaryRepository.create_entry(
            db=db,
            user_id=user_id,
            data= data
        )

    @staticmethod
    def get_entries(db:Session,user_id:int,skip:int=0,limit:int=10,start_date=None,end_date=None):
        return DiaryRepository.get_entries(
            db=db,
            user_id= user_id,
            skip=skip,
            limit=limit,
            start_date=start_date,
            end_date=end_date
        )

    @staticmethod
    def update_entry(db:Session,entry_id:int,data:DiaryEntryCreate):
        return DiaryRepository.update_entry(
            db=db,
            entry_id=entry_id,
            data=data
        )

    @staticmethod
    def delete_entry(db:Session,entry_id:int):
        return DiaryRepository.delete_entry(
            db=db,
            entry_id=entry_id
        )