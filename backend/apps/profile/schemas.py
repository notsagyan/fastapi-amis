from pydantic import (
    BaseModel,
    Field
)

from datetime import datetime

from typing import (
    Optional
)


class EmployeeSchema(BaseModel):
    id: Optional[int] = Field(
        None
    )
    first_name: str = Field(
        title="First Name"
    )
    middle_name: Optional[str] = Field(
        None,
        title="Middle Name"
    )
    last_name: str = Field(
        title="Last Name"
    )
    bio: str = Field(
        title="Biography describing the profile"
    )

    class Config:
        orm_mode = True
