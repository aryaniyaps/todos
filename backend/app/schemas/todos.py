from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoCreateSchema(BaseModel):
    content: str
    content: Optional[str] = None
    completed: Optional[bool] = False

    class Config:
        title = "TodoCreate"


class TodoUpdateSchema(BaseModel):
    content: Optional[str] = None
    completed: Optional[bool] = False

    class Config:
        title = "TodoUpdate"


class TodoSchema(BaseModel):
    id: int
    completed: bool
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        title = "Todo"
        orm_mode = True
