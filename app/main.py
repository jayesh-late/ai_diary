from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints.routers import api_router
from app.core.handler_registry import register_exception_handlers

app = FastAPI(
    title="Personal Progress API",
    description="Track daily learning and productivity",
    version="1.0"
)

# CORS configuration
origins = [
    "http://localhost:63342",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app=app)
Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def health_check():
    return {"status": "Diary API running"}



























































def seed_plans():
    from app.db.session import SessionLocal
    from app.db.models.subscription_model import SubscriptionPlan

    db = SessionLocal()

    if not db.query(SubscriptionPlan).first():
        plans = [
            SubscriptionPlan(name="FREE", price=0, description="Basic plan"),
            SubscriptionPlan(name="PRO", price=999, description="Analytics + AI"),
            SubscriptionPlan(name="PREMIUM", price=1999, description="All features")
        ]

        db.add_all(plans)
        db.commit()

    db.close()