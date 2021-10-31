from passlib.hash import argon2
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class User(Base):
    """Represents an individual user account."""

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )

    password = Column(
        String(255),
        nullable=False,
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
    )

    avatar = Column(
        String(255),
        default="default.jpg",
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
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

    todos = relationship(
        "Todo", back_populates="user", lazy="dynamic",
    )

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
