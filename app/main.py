# from fastapi import FastAPI
# from app.db.base import Base
# from app.db.session import engine
# from app.api.v1.endpoints.routers import api_router
#
# app = FastAPI(
#     title="Daily Diary API",
#     description="Track daily learning and productivity",
#     version="1.0"
# )
#
# Base.metadata.create_all(bind=engine)
# app.include_router(api_router)
#
# @app.get("/")
# def health_check():
#     return {"status": "Diary API running"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints.routers import api_router


app = FastAPI(
    title="Daily Diary API",
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

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def health_check():
    return {"status": "Diary API running"}