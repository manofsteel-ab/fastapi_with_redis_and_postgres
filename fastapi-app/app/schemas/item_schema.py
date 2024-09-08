from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    description: str
    data: dict
