
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.deps import DBSession
from app.schemas.auth_schema import UserSignup,UserResponse
from app.services.auth_service import AuthService

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

