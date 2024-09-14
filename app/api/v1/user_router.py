from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


@router.get("/user")
def get_item():
    return {
        "id": "RANDOM_USER_UUID",
        "first_name": "First",
        "last_name": "Last"
    }
