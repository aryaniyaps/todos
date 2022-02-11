from passlib.hash import bcrypt
from sqlalchemy import select

from app.database.core import db_session
from app.users.entities import User


class UserRepo:
    def get_user(self, user_id: int) -> User | None:
        """
        Get an user with the given ID.

        :param user_id: The user's ID.

        :return: The user with the given ID.
        """
        return db_session.get(User, user_id)


    def get_user_by_email(self, email: str) -> User | None:
        """
        Get an user with the given email.

        :param email: The user's email.

        :return: The user with the given email.
        """
        statement = select(User).filter(User.email == email)
        return db_session.scalars(statement).first()
        

    def create_user(self, email: str, password: str) -> User:
        """
        Create an user.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = User(email=email)
        user.password = bcrypt.hash(password)
        db_session.add(user)
        db_session.commit()
        return user

    def delete_user(self, user: User) -> None:
        """
        Delete the given user.

        :param user: The user to delete.
        """
        db_session.delete(user)
        db_session.commit()


user_repo = UserRepo()