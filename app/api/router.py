from fastapi import APIRouter
from .v1.item_router import router as item_router
from .v1.user_router import router as user_router

router = APIRouter()
router.include_router(item_router)
router.include_router(user_router)


@router.get("/health")
def health_check():
    return {"status": "healthy"}
