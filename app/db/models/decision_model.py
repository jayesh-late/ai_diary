from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship


class Decision(Base):

    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(Text)

    description = Column(Text)

    outcome = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User",back_populates="decisions")
