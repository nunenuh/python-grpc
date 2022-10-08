from pydantic import BaseModel

class Books(BaseModel):
    id: int
    title: str
    author: str
    description: str
    publisher: str