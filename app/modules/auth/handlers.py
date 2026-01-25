from sqlalchemy.orm import Session
from .models import User
from .schemas import CreateUserSchema
from .services import hash_password


def create_new_user(payload: CreateUserSchema, session: Session) -> User:

    new_user = User(username=payload.name, email=payload.email, password=hash_password(payload.password))
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
