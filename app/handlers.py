from sqlalchemy import text
from sqlalchemy.orm import Session
from .db import ENGINE
from .schemas import UserSchema

def create_new_user(request: dict) -> dict:
    with Session(ENGINE) as session:
        result = session.execute(
            text('INSERT INTO "user" (username, email) VALUES (:name, :email) RETURNING "user".id, username, email'),
            {"name": request["name"], "email": request["email"]}
        )
        session.commit()
        user = result.fetchone()
        new_user_data = UserSchema(id=user.id, name=user.username, email=user.email).model_dump()
        return new_user_data