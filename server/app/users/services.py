from app.errors import InvalidInput
from app.users.entities import User
from app.users.repositories import UserRepo


class UserService:
    @classmethod
    def create_user(cls, email: str, password: str) -> User:
        """
        Create an user.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = UserRepo.get_user_by_email(email=email)
        if user is not None:
            raise InvalidInput(
                message="User with that email already exists.",
            )
        return UserRepo.create_user(
            email=email, 
            password=password,
        )