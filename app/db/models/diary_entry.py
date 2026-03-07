from sqlalchemy import ForeignKey,Column,String,Integer,Date
from app.db.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class DailyEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"),index=True)
    date = Column(Date,nullable=False)
    task_completed = Column(String)
    hour_studied = Column(Integer)
    mood = Column(String)
    notes = Column(String)

    user = relationship("User",back_populates="diary_entries")

