from fastapi import FastAPI

from sqlalchemy import text
from sqlalchemy.orm import Session

from time import sleep
from .schemas import TestResponseSchema, UserSchema
from .services import generate_answer
from .db import init_db, get_db_session
from .handlers import create_new_user
from .settings import SETTINGS


app = FastAPI()
engine = init_db(SETTINGS.db.database_url)


async def emulate_async_operation(id, inc_str) -> str:
    sleep(5)
    return {"item_id": id, "q": inc_str}


@app.get("/", response_model=TestResponseSchema)
def read_root():
    return generate_answer()

@app.get("/db_health")
def db_health_check():
    with Session(engine) as session:
        version = session.execute(text('SELECT version()')).fetchone()
        return {"status": "healthy"}
    
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