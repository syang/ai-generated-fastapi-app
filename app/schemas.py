from pydantic import BaseModel
from datetime import date

class ItemBase(BaseModel):
    item_name: str
    item_price: float
    expiration_date: date

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
