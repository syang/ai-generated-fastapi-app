from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    item_price = Column(Float)
    expiration_date = Column(Date)
