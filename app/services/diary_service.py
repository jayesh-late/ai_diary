from fastapi import HTTPException,status
from app.repositories.diary_repository import DiaryRepository
from sqlalchemy.orm import Session
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
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entry Not Found"
            )

        if entry.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid Credentials"
            )
        return entry

    @staticmethod
    def get_entries(db:Session,user_id:int,skip:int=0,limit:int=10,start_date=None,end_date=None):
        entries = DiaryRepository.get_entries(
            db=db,
            user_id= user_id,
            skip=skip,
            limit=limit,
            start_date=start_date,
            end_date=end_date
        )
        for entry in entries:
            if entry.user_id!= user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail= "Invalid Credentials"
                )
        if not entries:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entry Not Found"
            )
        return entries

    @staticmethod
    def get_entry_by_id(db:Session,user_id:int,entry_id:int):
        entry = DiaryRepository.get_entry_by_id(
            db=db,
            entry_id=entry_id

        )
        if entry.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid Credentials"
            )

        if not entry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entry Not Found"
            )
        return entry

    @staticmethod
    def update_entry(db:Session,user_id:int,entry_id:int,data:DiaryEntryCreate):
        entry =  DiaryRepository.update_entry(
            db=db,
            entry_id=entry_id,
            data=data
        )
        if entry.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid Credentials"
            )
        if not entry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entry Not Found"
            )
        return entry


    @staticmethod
    def delete_entry(db: Session, user_id: int, entry_id: int):

        entry = DiaryRepository.get_entry_by_id(db, entry_id)

        if not entry:
            raise HTTPException(
                status_code=404,
                detail="Entry not found"
            )

        if entry.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )

        DiaryRepository.delete_entry(db, entry)

        return {"message": "Deleted"}

