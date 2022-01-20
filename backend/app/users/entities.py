from __future__ import annotations

from flask_login import UserMixin
from passlib.hash import argon2
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


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

    def set_password(self, password: str) -> None:
        """
        Sets an hashed version of the given password
        on the user instance.

        :param password: The password to set on the user.
        """
        self.password = argon2.hash(password)

    def check_password(self, password: str) -> bool:
        """
        Checks whether the given password and the user
        instance's password are the same.

        :param password: The password to check.
        """
        return argon2.verify(password, self.password)
