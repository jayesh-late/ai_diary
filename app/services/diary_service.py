from app.repositories.diary_repository import DiaryRepository
from sqlalchemy.orm import Session

from app.core.exceptions import InvalidCredentialsException,DiaryEntryNotFound
from app.schemas.diary_schema import DiaryEntryCreate

class DiaryService:
    @staticmethod
    def create_entry(db:Session,user_id:int,data:DiaryEntryCreate):

        entry = DiaryRepository.create_entry(
            db=db,
            user_id=user_id,
            data= data
        )
        if not entry:
            raise DiaryEntryNotFound()

        if entry.user_id != user_id:
            raise InvalidCredentialsException()
        return entry

    @staticmethod
    def get_entries(db:Session,
                    user_id:int,
                    page:int,
                    limit:int,
                    start_date=None,
                    end_date=None):

        offset = (page - 1) * limit
        entries = DiaryRepository.get_entries(
            db=db,
            user_id= user_id,
            offset= offset,
            page=page,
            limit=limit,
            start_date=start_date,
            end_date=end_date
        )
        if not entries:
            raise DiaryEntryNotFound()

        for entry in entries:
            if entry.user_id!= user_id:
                raise InvalidCredentialsException()

        total_entries = DiaryRepository.count_diary_entries(
            db = db,
            user_id = user_id
        )

        return {
            "items":entries,
            "total_entries":total_entries,
            "page":page,
            "limit":limit
        }



    @staticmethod
    def get_entry_by_id(db:Session,user_id:int,entry_id:int):
        entry = DiaryRepository.get_entry_by_id(
            db=db,
            entry_id=entry_id

        )
        if not entry:
            raise DiaryEntryNotFound()
        if entry.user_id != user_id:
            raise InvalidCredentialsException()


        return entry

    @staticmethod
    def update_entry(db:Session,user_id:int,entry_id:int,data:DiaryEntryCreate):
        entry =  DiaryRepository.update_entry(
            db=db,
            entry_id=entry_id,
            data=data
        )
        if not entry:
            raise DiaryEntryNotFound()

        if entry.user_id != user_id:
            raise InvalidCredentialsException()

        return entry


    @staticmethod
    def delete_entry(db: Session, user_id: int, entry_id: int):

        entry = DiaryRepository.get_entry_by_id(db, entry_id)

        if not entry:
            raise DiaryEntryNotFound()

        if entry.user_id != user_id:
            raise InvalidCredentialsException()

        DiaryRepository.delete_entry(db, entry)

        return {"message": "Deleted"}




