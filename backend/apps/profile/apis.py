from fastapi import APIRouter
from fastapi_amis_admin.globals.deps import (
    AsyncSess,
    SyncSess
)

from typing import List

from .models import Employee

from sqlalchemy import select

from core.globals import site


router = APIRouter()


@router.get("/employee/list", response_model=List[Employee])
async def list_employee():
    stmt = select(Employee).limit(10).order_by(Employee.id)
    result = await site.db.async_scalars(stmt)
    return result.all()
