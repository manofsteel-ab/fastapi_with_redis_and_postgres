from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.item_schema import ItemSchema
from app.services.item_service import create_item_service, get_item_service
from core.database import get_db

router = APIRouter()

@router.post("/items/")
async def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    item_id = await create_item_service(item, db)
    return {"item_id": item_id}

@router.get("/items/{item_id}")
async def get_item(item_id: str, db: Session = Depends(get_db)):
    item = await get_item_service(item_id, db)
    if item:
        return {"item": item}
    raise HTTPException(status_code=404, detail="Item not found")
