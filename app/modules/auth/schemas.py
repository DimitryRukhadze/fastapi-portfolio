import uuid

from pydantic import BaseModel, field_validator


class UserSchema(BaseModel):
    name: str
    email: str

class CreateUserSchema(UserSchema):
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        if not v:
            raise ValueError("Password required")
        return v

class UserOutputSchema(UserSchema):
    id: uuid.UUID
