from pydantic import BaseModel

class Socials(BaseModel):
    id: int
    name: str
    twitter: str