import pytest
from app.services.item_service import create_item_service, get_item_service
from app.models.item import Item
from core.database import SessionLocal
from core.redis_client import redis_client

@pytest.mark.asyncio
async def test_create_item_service(db_session):
    item = Item(id="test-id", name="test_item", description="A test item", data={})
    item_id = await create_item_service(item, db_session)
    assert item_id is not None
    assert redis_client.get(item_id) is not None

@pytest.mark.asyncio
async def test_get_item_service(db_session):
    item = Item(id="test-id", name="test_item", description="A test item", data={})
    db_session.add(item)
    db_session.commit()
    retrieved_item = await get_item_service(item.id, db_session)
    assert retrieved_item == item.json()
