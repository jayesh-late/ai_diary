from sqlalchemy import Column,ForeignKey,Integer,String,Date,Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id=Column(Integer,primary_key=True,index=True)
    habit_id=Column(Integer,ForeignKey("habits.id"))
    date=Column(Date)
    completed=Column(Boolean,default=True)

    habit =relationship("Habit",back_populates="logs")