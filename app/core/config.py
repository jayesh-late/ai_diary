from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DATABASE_URL: str = "sqlite:///./pie.db"
    SECRET_KEY :str = "supersecretkey"
    ALGORITHM :str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60


settings = Settings()