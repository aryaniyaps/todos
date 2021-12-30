from typing import Optional

from app.models.users import User
from app.services.base import BaseService


class UserService(BaseService):
    def user_by_email(self, *, email: str) -> Optional[User]:
        """
        Gets an user with the given email.

        :param email: The user's email.

        :return: The user with the given email.
        """
        return self.session.query(User).filter_by(email=email).first()

    def create_user(self, *, email: str, password: str) -> User:
        """
        Creates an user with the given data.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = User(email=email)
        user.set_password(password=password)
        self.session.add(user)
        self.session.commit()
        return user
