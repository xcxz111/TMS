from fastapi import APIRouter
from v0 import router as v0_router
from v1 import router as v1_router


router = APIRouter()
router.include_router(v0_router, prefix='/v0')
router.include_router(v1_router, prefix='/v1')

