from typing import Annotated
from app.db.deps import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

DBSession = Annotated[Session,Depends(get_db)]