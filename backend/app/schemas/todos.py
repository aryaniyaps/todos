from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    content: Optional[str] = None
    completed: Optional[bool] = False


class TodoCreate(TodoBase):
    content: str


class TodoUpdate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    completed: bool
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True