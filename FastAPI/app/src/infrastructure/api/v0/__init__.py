from fastapi import APIRouter
from .materials import router as material_router
from .health_check import router as health_check_router

router = APIRouter()
router.include_router(health_check_router, prefix='/health_check')
router.include_router(material_router, prefix='/material')

