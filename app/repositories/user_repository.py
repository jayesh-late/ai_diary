from sqlalchemy.orm import Session
from app.db.models.user_model import User
class UserRepository:

    @staticmethod
    def signup(db:Session,username:str,email:str,password:str):
        user = User(
            username=username,
            email=email,
            hashed_password=password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def login(db:Session,email:str):
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        return user

    @staticmethod
    def create_social_user(db, email: str, provider: str, provider_id: str):
        username = email.split("@")[0]

        user = User(
            email=email,
            username=username,
            hashed_password=None,
            provider=provider,
            provider_id=provider_id,
            is_active=True
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_user_by_provider_id(db:Session,provider:str,provider_id:str):
        user = db.query(User).filter(
            User.provider == provider,
            User.provider_id == provider_id,
        ).first()
        return user

