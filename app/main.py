from fastapi import FastAPI

from time import sleep


app = FastAPI()


async def emulate_async_operation(id, inc_str) -> str:
    sleep(5)
    return {"item_id": id, "q": inc_str}


@app.get("/")
def read_root():
    return  {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    complete = await emulate_async_operation(item_id, q)
    return complete
