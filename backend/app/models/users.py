from __future__ import annotations

from flask_login import UserMixin
from passlib.hash import argon2

from app.extensions import db


class User(db.Model, UserMixin):
    """Represents an individual user account."""

    id = db.Column(db.Integer, primary_key=True)

    password = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(255), unique=True, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=db.func.now(),
        server_default=db.func.now(),
        nullable=False,
    )

    todos = db.relationship("Todo", back_populates="user")

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
