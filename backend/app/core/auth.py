from binascii import hexlify
from os import urandom
from typing import Optional

from flask_httpauth import HTTPTokenAuth

from app.models.users import User

__all__ = ("auth", "create_auth_token", "remove_auth_token", "check_auth_token")


auth = HTTPTokenAuth()


def create_auth_token(user: User, length: int = 20) -> str:
    """
    Creates and stores an authentication token.

    :param user: The user to create the token for.
    :param length: The length of the auth token.
    :return: The created auth token.
    """
    user.auth_token = hexlify(urandom(length)).decode()
    return user


def remove_auth_token(user: User) -> None:
    """
    Removes the authentication token given.

    :param user: The user to remove the auth token for.
    """
    user.auth_token = None
    return user


@auth.verify_token
def check_auth_token(token: Optional[str]) -> Optional[User]:
    """
    Checks and gets the user associated with the
    given auth token, if they exist.

    :param token: The auth token to check.
    
    :return: The user associated with the auth token.
    """
    if token is not None:
        return User.check_auth_token(token) 
    return None
