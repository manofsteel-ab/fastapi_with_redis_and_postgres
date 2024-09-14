from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


@router.get("/item")
def get_item():
    return {
        "id": "RANDOM_UUID",
        "name": "Item name"
    }
