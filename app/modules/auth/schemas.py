import uuid

from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str
    email: str
    password: Optional[str] = None
