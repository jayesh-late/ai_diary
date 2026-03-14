from pydantic import BaseModel


class SubscriptionPlanResponse(BaseModel):

    id: int
    name: str
    price: int
    description: str

    class Config:
        from_attributes = True


class SubscribeRequest(BaseModel):

    plan_id: int