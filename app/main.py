from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text, select
from argon2.exceptions import VerifyMismatchError

from .schemas import TestResponseSchema, UserSchema
from .services import generate_answer
from .db import init_db, get_db_session, User
from .handlers import create_new_user
from .settings import SETTINGS


app = FastAPI()
engine = init_db(SETTINGS.db.database_url)


@app.get("/", response_model=TestResponseSchema)
def read_root():
    return generate_answer()
    
@app.get("/users", response_model=list[UserSchema] | None)
def get_users(session: Session = Depends(get_db_session)):
    result = session.scalars(select(User)).all()
    users = [UserSchema(id=row.id, name=row.username, email=row.email) for row in result]
    return users

@app.post("/users", response_model=UserSchema)
def create_user(user: UserSchema, session: Session = Depends(get_db_session)):
    try:
        created_user = create_new_user(user.model_dump(), session=session)
    except VerifyMismatchError:
        return {"message": "Password verification failed", "status": "error"}
    except ValueError as ve:
        return {"message": str(ve), "status": "error"}
    return created_user