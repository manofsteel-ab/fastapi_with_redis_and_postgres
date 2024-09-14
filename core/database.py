from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from .config import settings
from sqlalchemy.schema import MetaData

# Metadata configuration with naming conventions for consistency
metadata = MetaData(naming_convention={
    "pk": "pk_%(table_name)s",
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
})

# Create the SQLAlchemy engine
engine = create_engine(settings.database_url, echo=settings.debug)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models with metadata configuration
Base = declarative_base(metadata=metadata)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a SQLAlchemy session.

    Yields:
        Session: A SQLAlchemy session object.
    """
    db: Session = SessionLocal()
    try:
        yield db
    except Exception as e:
        # Optionally, you could log the exception here
        raise e
    finally:
        db.close()
