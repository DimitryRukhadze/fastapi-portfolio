from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from argon2.exceptions import VerifyMismatchError

from app.services import generate_answer
from app.modules.auth.schemas import UserSchema, CreateUserSchema, UserOutputSchema
from app.core.database import init_db, get_db_session
from app.modules.auth.models import User
from app.modules.auth.handlers import create_new_user
from app.settings import SETTINGS


app = FastAPI()
engine = init_db(SETTINGS.db.database_url)


@app.get("/", response_model=UserSchema)
def read_root():
    return generate_answer()
    
@app.get("/users", response_model=list[UserOutputSchema] | None)
def get_users(session: Session = Depends(get_db_session)):
    result = session.scalars(select(User)).all()
    users = [UserOutputSchema(id=row.id, name=row.username, email=row.email) for row in result]
    return users

@app.post("/users", response_model=UserOutputSchema)
def create_user(user: CreateUserSchema, session: Session = Depends(get_db_session)):
    created_user = create_new_user(user, session=session)
    return created_user