import requests
from jose import jwt
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.repositories.user_repository import UserRepository
from app.core.exceptions import InvalidAppleTokenException

APPLE_KEY_URL = "https://appleid.apple.com/auth/keys"

class AppleAuthService:

    @staticmethod
    def apple_login(db:Session,token:str):
        apple_key = requests.get(APPLE_KEY_URL).json()
        headers = jwt.get_unverified_header(token)

        key = None

        for k in apple_key["keys"]:
            if k["kid"] == headers["kids"]:
                key = k
                break

        if not key :
            raise InvalidAppleTokenException()

        payload = jwt.decode(
            token=token,
            key=key,
            algorithms=["RS256"],
            audience="YOUR_APPLE_CLIENT_ID"
        )

        provider_id = payload.get("sub")
        email = payload.get("email")

        user = UserRepository.get_user_by_provider_id(
            db=db,
            provider_id=provider_id,
            provider="apple"
        )
        if not user:
            user = UserRepository.create_social_user(
                db=db,
                email=email,
                provider="apple",
                provider_id=provider_id
            )
        access_token = create_access_token(
            data={"user_id":user.id}
        )
        return access_token