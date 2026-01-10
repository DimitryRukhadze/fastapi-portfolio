import uuid

from pydantic import BaseModel
from typing import Optional


class TestResponseSchema(BaseModel):
    message: str
    status: str


class UserSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str
    email: str