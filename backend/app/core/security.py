from binascii import hexlify
from os import urandom
from typing import Optional

from app.extensions import redis_store
from app.models.users import User


def create_auth_token(user: User, length: int = 20) -> str:
    """
    Creates and stores an authentication token.

    :param user: The user to create the token for.
    :param length: The length of the auth token.
    :return: The created auth token.
    """
    token = hexlify(urandom(length)).decode()
    redis_store.set(token, user.id)
    return token


def remove_auth_token(token: str) -> None:
    """
    Removes the authentication token given.

    :param token: The auth token to remove.
    """
    redis_store.delete(token)


def check_auth_token(token: Optional[str]) -> Optional[User]:
    """
    Checks and gets the user associated with the
    given auth token, if they exist.

    :param token: The auth token to check.
    
    :return: The user associated with the auth token.
    """
    user_id = redis_store.get(token)
    if user_id is None:
        return None
    return User.query.get(user_id)
