
from sqlalchemy import Column, DateTime, Boolean, func, String
from sqlalchemy.orm import Session
from typing import Type
import uuid


from ...core.database import Base

class CustomBaseModel(Base):
    __abstract__ = True  # This class will not have a corresponding table

    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    @classmethod
    def get_table_name(cls) -> str:
        """Return the table name of the model."""
        return cls.__tablename__

    @classmethod
    def save(cls, session: Session, instance) -> None:
        """Save an instance to the database."""
        session.add(instance)
        session.commit()

    @classmethod
    def delete(cls, session: Session, instance) -> None:
        """Delete an instance from the database."""
        session.delete(instance)
        session.commit()

    @classmethod
    def get_by_id(cls: Type['CustomBaseModel'], session: Session, id_: int):
        """Get an instance by its ID."""
        return session.query(cls).filter_by(id=id_).first()
