from fastapi import APIRouter
from api.routes import general



router = APIRouter()
router.include_router(general.router, tags=["general service"], prefix="/v1")
