from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints.routers import api_router

app = FastAPI(
    title="Daily Diary API",
    description="Track daily learning and productivity",
    version="1.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(api_router)

@app.get("/")
def health_check():
    return {"status": "Diary API running"}
