from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Habit(Base):

    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String)

    description = Column(String)

    is_active = Column(Boolean, default=True)

    user = relationship("User",back_populates="habits")