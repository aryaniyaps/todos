from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Todo(Base):
    """Represents an user's todo."""

    id = Column(Integer, primary_key=True)

    content = Column(Text, nullable=False)

    completed = Column(Boolean, default=False, nullable=False)

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

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )

    user = relationship("User", back_populates="todos")

    __tablename__ = "todos"

    def __repr__(self) -> str:
        return f"Todo <{self.content[:25]}>"
