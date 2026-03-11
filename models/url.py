from pydantic import BaseModel

class URL(BaseModel):
    longURL: str
