from pydantic import BaseModel


class TestResponseSchema(BaseModel):
    message: str
    status: str