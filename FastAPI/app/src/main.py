from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic.error_wrappers import ValidationError
from src.infrastructure.api import router as api_router


app = FastAPI(
    title=f'TMS',
    description='test project',
    version='0.0.0',
    debug=True
)


app.include_router(api_router, prefix='/api')
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)