from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DATABASE_URL: str = "sqlite:///./jayesh.db"
    SECRET_KEY :str = "supersecretkey"
    ALGORITHM :str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60
    GOOGLE_CLIENT_ID :str = "492629886649-kphnmbe9boia6v4op71ns5vuc0fgi8bj.apps.googleusercontent.com"


settings = Settings()