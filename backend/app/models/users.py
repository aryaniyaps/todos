from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreateInput(BaseModel):
    email: EmailStr
    password: str

    class Config:
        title = "UserCreateInput"


class UserModel(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        title = "User"
        orm_mode = True
