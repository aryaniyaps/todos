from app.models.users import User
from app.services.base import BaseService


class AuthService(BaseService):
    def create_access_token(self, *, user: User) -> str:
        """
        Creates an access token for the given user.

        :param user: The user to create the access token for.

        :return: The created access token.
        """
        pass