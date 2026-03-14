from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.repositories.subscription_repository import SubscriptionRepository
from app.core.exceptions import SubscriptionPlanNotFoundException

class SubscriptionService:

    @staticmethod
    def list_plans(db:Session):
        return SubscriptionRepository.get_all_plans(db=db)

    @staticmethod
    def get_user_subscription(db:Session,user_id:int):
        return SubscriptionRepository.get_user_subscription(db=db,user_id=user_id)

    @staticmethod
    def subscribe_user(db:Session,user_id:int,plan_id:int):
        # 1.validate_plan
        plan = SubscriptionRepository.get_plan_by_id(
            db = db,
            plan_id= plan_id
        )
        if not plan:
            raise SubscriptionPlanNotFoundException()

        # 2. deactivate current subscription
        SubscriptionRepository.deactivate_user_subscription(
            db=db,
            user_id=user_id,
        )

        # 3. create new subscription
        subscription = SubscriptionRepository.create_subscription(
            db=db,
            user_id=user_id,
            plan_id=plan_id
        )
        return subscription



