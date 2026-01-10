from fastapi import FastAPI

from sqlalchemy import text
from sqlalchemy.orm import Session

from time import sleep
from .schemas import TestResponseSchema
from .services import generate_answer
from .db import ENGINE


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

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    complete = await emulate_async_operation(item_id, q)
    return complete

