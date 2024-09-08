from sqlalchemy.orm import Session
from app.models.item import Item
from core.redis_client import redis_client
from core.utils import generate_id

async def create_item_service(item, db: Session):
    item_id = generate_id()
    db_item = Item(id=item_id, name=item.name, description=item.description, data=item.data)
    db.add(db_item)
    db.commit()
    redis_client.set(item_id, item.json())
    return item_id

async def get_item_service(item_id: str, db: Session):
    item_data = redis_client.get(item_id)
    if item_data:
        return item_data.decode('utf-8')
    item_data = db.query(Item).filter(Item.id == item_id).first()
    if item_data:
        redis_client.set(item_id, item_data)
        return item_data
    return None
