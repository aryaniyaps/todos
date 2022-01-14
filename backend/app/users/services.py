from typing import Optional

from sqlalchemy import select

from app.core.database import db_session
from app.users.entities import User


class UserService:
    def user_by_email(self, *, email: str) -> Optional[User]:
        """
        Gets an user with the given email.

        :param email: The user's email.

        :return: The user with the given email.
        """
        statement = select(User).filter_by(email=email)
        return db_session.scalars(statement).first()

    def create_user(self, *, email: str, password: str) -> User:
        """
        Creates an user with the given data.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = User(email=email)
        user.set_password(password=password)
        db_session.add(user)
        db_session.commit()
        return user
