from typing import Optional

from app.users.entities import User


class AuthService:
    def create_access_token(self, *, user: User) -> str:
        """
        Creates an access token for the given user.

        :param user: The user to create the access token for.

        :return: The created access token.
        """
        pass

    def revoke_access_token(self, *, access_token: str) -> None:
        """
        Revokes the given access token.

        :param access_token: The access token to revoke.
        """
        pass

    def user_from_access_token(self, *, access_token: str) -> Optional[User]:
        """
        Gets the user from the given access token.

        :param access_token: The token to get the user from.

        :return: The user associated with the access token.
        """
        pass