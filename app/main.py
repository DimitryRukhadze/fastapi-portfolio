from fastapi import FastAPI

from sqlalchemy import text

from .schemas import TestResponseSchema, UserSchema
from .services import generate_answer
from .db import init_db, get_db_session
from .handlers import create_new_user
from .settings import SETTINGS


app = FastAPI()
engine = init_db(SETTINGS.db.database_url)


@app.get("/", response_model=TestResponseSchema)
def read_root():
    return generate_answer()
    
@app.get("/users", response_model=list[UserSchema] | None)
def get_users():
    session = next(get_db_session())
    result = session.execute(text('SELECT id, username, email FROM "user"')).all()
    print(type(result[-1]))
    users = [UserSchema(id=row.id, name=row.username, email=row.email) for row in result]
    return users

@app.post("/users", response_model=UserSchema)
def create_user(user: UserSchema):
    create_new_user(user.model_dump(), next(get_db_session()))