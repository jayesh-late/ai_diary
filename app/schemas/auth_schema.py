from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
class UserSignup(BaseModel):
    email:EmailStr
    username:str
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenResponse(BaseModel):
    access_access:str
    token_type:str = "bearer"

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    username:str
    is_active:bool
    created_at:datetime

    model_config = ConfigDict(
        from_attributes=True
    )