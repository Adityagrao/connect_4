from fastapi import APIRouter
from .controller import connect

api_router = APIRouter()
api_router.include_router(connect.router, prefix="/connect", tags=["Connect 4"])
