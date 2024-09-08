import pytest
from unittest.mock import MagicMock
from app.services.item_service import create_item_service, get_item_service
from app.models.item import Item

@pytest.mark.asyncio
async def test_create_item_service(db_session):
    # Mock Redis client
    redis_client.set = MagicMock()
    item = Item(id="test-id", name="test_item", description="A test item", data={})
    item_id = await create_item_service(item, db_session)
    assert item_id == "test-id"
    redis_client.set.assert_called_once_with("test-id", item.json())

@pytest.mark.asyncio
async def test_get_item_service(db_session):
    # Mock Redis client
    redis_client.get = MagicMock(return_value=None)
    db_session.query = MagicMock(return_value=[Item(id="test-id", name="test_item", description="A test item", data={})])
    retrieved_item = await get_item_service("test-id", db_session)
    assert retrieved_item == '{"id": "test-id", "name": "test_item", "description": "A test item", "data": {}}'
