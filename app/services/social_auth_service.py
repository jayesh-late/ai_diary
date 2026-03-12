
from fastapi import HTTPException,status

from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token
from sqlalchemy.orm import Session

from google.oauth2 import id_token
from google.auth.transport import requests
from google.auth.exceptions import GoogleAuthError

class GoogleAuthService:

    @staticmethod
    def google_login(db:Session,token:str):
        id_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            settings.GOOGLE_CLIENT_ID
        )

        if not id_info:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid Google token")

        provider_id = id_info.get("sub")
        email = id_info.get("email")
        email_verified = id_info.get("email_verified")

        if not email_verified:
            raise ValueError("Google email not verified")

        user = UserRepository.get_user_by_provider_id(
            db=db,
            provider="google",
            provider_id=provider_id
        )

        if not user:
            user = UserRepository.create_social_user(
                db=db,
                email=email,
                provider="google",
                provider_id=provider_id
            )

        access_token = create_access_token(
            data={"user_id":user.id}
        )
        return access_token