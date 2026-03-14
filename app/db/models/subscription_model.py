from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True)
    price = Column(Integer)
    description = Column(String)
    is_active = Column(Boolean,default=True)

    subscriptions = relationship("UserSubscription", back_populates="plan")


class UserSubscription(Base):
    __tablename__ = "user_subscription"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    plan_id = Column(Integer,ForeignKey("subscription_plans.id"))
    start_date = Column(DateTime(timezone=True),server_default=func.now())
    end_date = Column(DateTime,nullable=True)
    is_active = Column(Boolean,default=True)

    user = relationship("User", back_populates="subscription")
    plan = relationship("SubscriptionPlan",back_populates="subscriptions")