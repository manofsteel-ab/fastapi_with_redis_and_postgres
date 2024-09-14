from sqlalchemy import Column, String

from . import CustomBaseModel


class User(CustomBaseModel):
    __tablename__ = 'users'

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
