from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import Annotated ,List
from app.db.models.user_model import User
from app.core.deps import get_db,get_current_user
from app.services.subscription_service import SubscriptionService
from app.schemas.subscription_schema import SubscriptionPlanResponse,SubscribeRequest

DBSession = Annotated[Session,Depends(get_db)]
UserSession =Annotated[User,Depends(get_current_user)]

router = APIRouter()

@router.get("/plans", response_model=List[SubscriptionPlanResponse])
async def list_plans(db:DBSession):

    plans = SubscriptionService.list_plans(db=db)

    return plans


@router.get("/me")
async def get_my_subscription(db:DBSession,current_user:UserSession):
    subscription = SubscriptionService.get_user_subscription(
        db = db,
        user_id=current_user.id
    )
    return subscription

@router.post("/subscribe")
async def subscribe_user(db:DBSession,data:SubscribeRequest,current_user:UserSession):
    subscription = SubscriptionService.subscribe_user(
        db=db,
        plan_id=data.plan_id,
        user_id=current_user.id
    )
    return {
        "message": "Subscription activated",
        "subscription_id": subscription.id
    }
