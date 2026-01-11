from fastapi import FastAPI

from sqlalchemy import text
from sqlalchemy.orm import Session

from time import sleep
from .schemas import TestResponseSchema, UserSchema
from .services import generate_answer
from .db import ENGINE
from .handlers import create_new_user


app = FastAPI()


async def emulate_async_operation(id, inc_str) -> str:
    sleep(5)
    return {"item_id": id, "q": inc_str}


@app.get("/", response_model=TestResponseSchema)
def read_root():
    return generate_answer()

@app.get("/db_health")
def db_health_check():
    print(ENGINE)
    with Session(ENGINE) as session:
        version = session.execute(text('SELECT version()')).fetchone()
        return {"status": "healthy"}
    
@app.get("/users", response_model=list[UserSchema])
def get_users():
    with Session(ENGINE) as session:
        result = session.execute(text('SELECT id, username, email FROM "user"')).all()
        users = [UserSchema(id=row.id, username=row.username, email=row.email) for row in result]
        return users

@app.post("/users", response_model=UserSchema)
def create_user(user: UserSchema):
    create_new_user(user.model_dump())