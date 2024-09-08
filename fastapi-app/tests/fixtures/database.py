from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base
from core.config import settings

# Create an engine and session for test database
TEST_DATABASE_URL = "postgresql://user:password@localhost:5432/testdatabase"
engine = create_engine(TEST_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)
