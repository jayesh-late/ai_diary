from app.db.base import Base
from sqlalchemy import String,Column,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    created_at = Column(DateTime,onupdate=datetime.utcnow)

    diary_entries = relationship("DailyEntry",back_populates="user")

