from app.exceptions import InvalidUsage
from app.users.entities import User
from app.users.services import user_service


class AuthService:
    def authenticate_user(self, email: str, password: str) -> User:
        """
        Checks the given credentials.

        :param email: The user's email.

        :param password: The user's password.

        :return: The authenticated user.
        """
        user = user_service.user_by_email(email=email)
        authenticated = (
            user is not None and 
            user.check_password(password=password)
        )
        if not authenticated:
            raise InvalidUsage(
                message="Invalid credentials given.",
            )
        return user


auth_service = AuthService()