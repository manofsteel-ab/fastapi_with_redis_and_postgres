from sqlalchemy import Column, String, JSON
from core.database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    data = Column(JSON)
