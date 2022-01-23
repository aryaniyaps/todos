from typing import Optional

from sqlalchemy import select

from app.database import db_session
from app.errors import InvalidUsage
from app.users.entities import User


class UserService:
    def user_by_email(self, email: str) -> Optional[User]:
        """
        Gets an user with the given email.

        :param email: The user's email.

        :return: The user with the given email.
        """
        statement = select(User).filter_by(email=email)
        return db_session.scalars(statement).first()

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Gets an user with the given ID.

        :param user_id: The user's ID.

        :return: The user with the given ID.
        """
        return db_session.get(User, user_id)

    def create_user(self, email: str, password: str) -> User:
        """
        Creates an user with the given data.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = self.user_by_email(email=email)
        if user is not None:
            raise InvalidUsage(
                message="User with that email already exists.",
            )
        user = User(email=email)
        user.set_password(password=password)
        db_session.add(user)
        db_session.commit()
        return user


user_service = UserService()