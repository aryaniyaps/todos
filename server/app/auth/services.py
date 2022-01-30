from passlib.hash import bcrypt

from app.errors import InvalidInput
from app.users.entities import User
from app.users.services import user_service


class AuthService:
    def authenticate(self, email: str, password: str) -> User:
        """
        Check the given user credentials.

        :param email: The user's email.

        :param password: The user's password.

        :return: The authenticated user.
        """
        user = user_service.user_by_email(email=email)
        if (
            user is None or not 
            bcrypt.verify(password, user.password)
        ):
            raise InvalidInput(
                message="Invalid credentials given.",
            )
        return user


auth_service = AuthService()