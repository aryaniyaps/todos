from typing import Optional

from app.models.users import User


def create_auth_token(user: User) -> str:
    """
    Creates and stores an authentication token.

    :param user: The user to create the token for.
    :return: The created auth token.
    """
    pass


def remove_auth_token(user: User) -> None:
    """
    Removes the authentication token stored for
    the given user, if it exists.

    :param user: THe user to remove the token for.
    """
    pass


def check_auth_token(token: str) -> Optional[User]:
    """
    Checks and gets the user associated with the
    given auth token, if they exist.

    :param token: The auth token to check.
    :return: The associated user.
    """
    pass
