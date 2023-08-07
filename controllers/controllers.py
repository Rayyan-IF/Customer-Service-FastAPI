from fastapi import APIRouter
from services.services import getAll_customers

router = APIRouter()

@router.get("/customers")
async def get_all():
    return getAll_customers()