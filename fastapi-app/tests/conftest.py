import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base
from core.config import settings

# Test database URL
TEST_DATABASE_URL = "postgresql://user:password@localhost:5432/testdatabase"

# Create engine for testing
engine = create_engine(TEST_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    # Create the test database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the test database schema
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
