from __future__ import annotations

from flask_login import UserMixin
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.core import Base


class User(UserMixin, Base):
    """Represents an individual user account."""

    id = Column(Integer, primary_key=True)

    password = Column(String(255), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

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

    todos = relationship("Todo", back_populates="user")

    __tablename__ = "users"

    def __repr__(self) -> str:
        return f"User <{self.email}>"
