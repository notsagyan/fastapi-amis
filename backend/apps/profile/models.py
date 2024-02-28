from typing import Optional
from sqlalchemy import (
    Column,
    DateTime,
    func
)

from fastapi_amis_admin import amis

from fastapi_amis_admin.models import Field, SQLModel

from datetime import datetime


class Employee(SQLModel, table=True):
    __tablename__ = 'employee'

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False
    )
    first_name: str = Field(
        title='First Name',
        nullable=False,
    )
    middle_name: Optional[str] = Field(
        None,
        title='Middle Name',
        nullable=True,
    )
    last_name: str = Field(
        title='Last Name',
        nullable=False,
    )
    bio: str = Field(
        default='',
        title='Biography',
        amis_form_item=amis.Textarea()
    )
    is_active: bool = Field(
        False,
        title='Is Active'
    )
    join_date: Optional[datetime] = Field(
        title="Created at",
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=True
        )
    )
