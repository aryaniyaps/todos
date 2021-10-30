from sqlalchemy import Column, ForeignKey, Text, Boolean, Integer, DateTime
from sqlalchemy.sql import func

from backend.database import Base


class Todo(Base):
    """Represents an user's todo."""

    __tablename__ = "todos"

    id = Column(
        Integer,
        primary_key=True,
    )

    content = Column(
        Text,
        nullable=False,
    )

    completed = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"Todo <{self.content[:25]}>"