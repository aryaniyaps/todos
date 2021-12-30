from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    completed: Optional[bool] = False

    class Config:
        title = "UserCreate"


class UserSchema(BaseModel):
    id: int
    email: EmailStr
    completed: bool = False
    created_at: datetime
    updated_at: datetime

    class Config:
        title = "User"
        orm_mode = True
