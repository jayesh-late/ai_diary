from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from app.core.security import hash_password,verify_password,create_access_token
from app.core.exceptions import InvalidCredentialsException,EmailNotAcceptableException


class AuthService:

    @staticmethod
    def signup(db:Session,username:str,email:str,password:str):
        existing_user = UserRepository.login(
            db=db,
            email=email
        )

        if existing_user:
            raise EmailNotAcceptableException()

        hashed = hash_password(password)

        user = UserRepository.signup(
            db=db,
            username=username,
            email=email,
            password=hashed
        )
        return user

    @staticmethod
    def login(db:Session,email:str,password:str):
        user = UserRepository.login(
            db=db,
            email=email,
        )

        if not user :
            raise InvalidCredentialsException()

        if not verify_password(password,user.hashed_password):
            raise InvalidCredentialsException()

        token = create_access_token({"user_id":user.id})

        return token
