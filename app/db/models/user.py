from app.db.base import Base
from sqlalchemy import String,Column,Integer,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,nullable=False)
    hashed_password = Column(String,nullable=False)

    