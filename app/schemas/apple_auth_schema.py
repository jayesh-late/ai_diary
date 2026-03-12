from pydantic import BaseModel

class AppleAuthRequest(BaseModel):
    id_token: str