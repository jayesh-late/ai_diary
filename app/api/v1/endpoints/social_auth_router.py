from fastapi import APIRouter,status,HTTPException,Depends
from typing import Annotated
from sqlalchemy.orm import Session

from app.schemas.social_auth_schema import GoogleAuthRequest,TokenResponse
from app.services.social_auth_service import GoogleAuthService
from app.services.apple_auth_service import AppleAuthService
from app.core.deps import get_db

DBSession =Annotated[Session,Depends(get_db)]
router = APIRouter()

@router.post("/google",response_model=TokenResponse)
async def google_login(data:GoogleAuthRequest,db:DBSession):

    access_token = GoogleAuthService.google_login(
        db=db,
        token= data.id_token,
    )

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Google token"
        )

    return {
            "access_token": access_token,
            "token_type": "bearer"
        }

@router.post("/apple")
async def apple_login(token:str,db:DBSession):
    access_token = AppleAuthService.apple_login(
        db=db,
        token=token
    )
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }