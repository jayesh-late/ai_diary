
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth_schema import UserSignup,UserResponse
from app.services.auth_service import AuthService
from app.core.deps import get_db,get_current_user
from typing import Annotated
from sqlalchemy.orm import Session
from app.db.models.user_model import User
DBSession = Annotated[Session,Depends(get_db)]
UserSession = Annotated[User,Depends(get_current_user)]


router = APIRouter()

@router.post("/signup",response_model=UserResponse)
async def signup(db:DBSession,data:UserSignup):
    user = AuthService.signup(
        db=db,
        username=data.username,
        email=str(data.email),
        password= data.password
    )
    return user

@router.post("/login")
async def login(db:DBSession,data: OAuth2PasswordRequestForm = Depends()):
    token = AuthService.login(
        db=db,
        email=str(data.username),
        password=data.password
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }

