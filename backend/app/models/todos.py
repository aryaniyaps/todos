from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoCreateInput(BaseModel):
    content: str


class TodoUpdateInput(BaseModel):
    content: Optional[str]
    completed: Optional[bool]


class TodoModel(BaseModel):
    id: int
    completed: bool
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        title = "Todo"
        orm_mode = True
