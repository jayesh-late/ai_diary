from fastapi import HTTPException,status

from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from app.core.security import hash_password,verify_password,create_access_token
from app.schemas.auth_schema import UserSignup,UserLogin
class AuthService:

    @staticmethod
    def signup(db:Session,username:str,email:str,password:str):
        existing_user = UserRepository.login(
            db=db,
            email=email
        )

        if existing_user:
            raise HTTPException (
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Email Already Registered "
            )

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
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )

        if not verify_password(password,user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )

        token = create_access_token({"user_id":user.id})

        return token
