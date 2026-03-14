from sqlalchemy.orm import Session
from app.db.models.subscription_model import UserSubscription,SubscriptionPlan

class SubscriptionRepository:

    @staticmethod
    def get_all_plans(db:Session):
        return db.query(SubscriptionPlan).filter(SubscriptionPlan.is_active == True).all()

    @staticmethod
    def get_plan_by_id(db:Session,plan_id:int):
        return db.query(UserSubscription).filter(UserSubscription.plan_id == plan_id).first()

    @staticmethod
    def get_user_subscription(db:Session,user_id:int):
        return (db.query(UserSubscription)
                .filter(UserSubscription.user_id == user_id,
                        UserSubscription.is_active == True
                        )
                .first())

    @staticmethod
    def deactivate_user_subscription(db:Session,user_id:int):
        subscription = (db.query(UserSubscription)
                .filter(UserSubscription.user_id == user_id,
                        UserSubscription.is_active == True)
                .first()
                )
        if subscription :
            subscription.is_active == False
            db.commit()
        return subscription

    @staticmethod
    def create_subscription(db:Session,user_id:int,plan_id:int):
        subscription = UserSubscription(
            user_id=user_id,
            plan_id=plan_id,
            is_active= True
        )
        db.add(subscription),
        db.commit()
        db.refresh(subscription)

        return subscription