from app.errors import InvalidInput
from app.users.entities import User
from app.users.repositories import user_repo


class UserService:
    def create_user(self, email: str, password: str) -> User:
        """
        Create an user.

        :param email: The user's email.

        :param password: The user's password.

        :return: The created user.
        """
        user = user_repo.by_email(email=email)
        if user is not None:
            raise InvalidInput(
                message="User with that email already exists.",
            )
        return user_repo.create(
            email=email, 
            password=password,
        )


user_service = UserService()