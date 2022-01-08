from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoCreateInput(BaseModel):
    content: str
    content: Optional[str] = None
    completed: Optional[bool] = False

    class Config:
        title = "TodoCreateInput"


class TodoUpdateInput(BaseModel):
    content: Optional[str] = None
    completed: Optional[bool] = False

    class Config:
        title = "TodoUpdateInput"


class TodoModel(BaseModel):
    id: int
    completed: bool
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        title = "Todo"
        orm_mode = True
