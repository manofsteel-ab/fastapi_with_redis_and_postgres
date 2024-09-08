import pytest
from fastapi.testclient import TestClient
from app.main import app
from core.redis_client import redis_client
from core.database import SessionLocal
from app.models.item import Item
from sqlalchemy import create_engine

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Clear database and Redis before each test
    db = SessionLocal()
    db.query(Item).delete()
    db.commit()
    redis_client.flushdb()
    yield
    # Clear database and Redis after each test
    db.query(Item).delete()
    db.commit()
    redis_client.flushdb()


def test_create_item():
    response = client.post("/items/", json={"name": "test_item", "description": "A test item", "data": {}})
    assert response.status_code == 200
    assert "item_id" in response.json()


def test_get_item():
    # Create item
    response = client.post("/items/", json={"name": "test_item", "description": "A test item", "data": {}})
    item_id = response.json()["item_id"]

    # Get item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item"] == '{"name": "test_item", "description": "A test item", "data": {}}'
