from app.db.base import Base
from sqlalchemy import String,Column,Integer,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import  datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)

    username = Column(String, nullable=True)          # changed
    hashed_password = Column(String, nullable=True)   # changed

    provider = Column(String, nullable=False, default="local")
    provider_id = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    daily_entries = relationship("DailyEntry", back_populates="user")
    habits = relationship("Habit", back_populates="user")
    decisions = relationship("Decision", back_populates="user")