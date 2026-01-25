from sqlalchemy import text
from sqlalchemy.orm import Session
from .schemas import UserSchema
from .services import hash_password


def create_new_user(request: dict, session: Session) -> dict:
    if not request.get("password", None):
        raise ValueError("Password required")

    hashed_password = hash_password(request["password"])
    result = session.execute(
        text('INSERT INTO "user" (username, email, password) VALUES (:name, :email, :hashed_password) RETURNING "user".id, username, email'),
        {"name": request["name"], "email": request["email"], "hashed_password": hashed_password},
    )
    session.commit()
    user = result.fetchone()
    new_user_data = UserSchema(id=user.id, name=user.username, email=user.email).model_dump()
    return new_user_data
