from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_material():
    return {'name': 'test_material', 'lesson_url': 'test_url'}
