from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    ForeignKey, 
    Integer, 
    Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.core import Base


class Todo(Base):
    """
    Represents an user's todo.
    """

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True, 
    )

    user_id = Column(
        Integer,
        ForeignKey(
            column="users.id", 
            ondelete="CASCADE", 
            onupdate="CASCADE",
        ),
        primary_key=True,
    )

    content = Column(Text, nullable=False)

    completed = Column(
        Boolean, 
        default=False, 
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
