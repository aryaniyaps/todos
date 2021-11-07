from binascii import hexlify
from hashlib import sha256
from os import urandom
from typing import Optional

from app.extensions import redis_store
from app.models.users import User


def generate_auth_token() -> str:
    """
    Generates a new authentication token.

    :return: The generated auth token.
    """
    return hexlify(urandom(20)).decode()


def create_auth_token(user_id: int) -> str:
    """
    Creates and stores an authentication token.

    :param user_id: The user ID to create the token for.
    :return: The created auth token.
    """
    token = generate_auth_token()
    token_hash = sha256(token).hexdigest()
    redis_store.set(token_hash, user_id)
    return token


def remove_auth_token(user: User) -> None:
    """
    Removes the authentication token stored for
    the given user, if it exists.

    :param user: The user to remove the token for.
    """
    pass


def check_auth_token(token: str) -> Optional[User]:
    """
    Checks and gets the user associated with the
    given auth token, if they exist.

    :param token: The auth token to check.
    :return: The associated user.
    """
    token_hash = sha256(token).hexdigest()
    user_id = redis_store.get(token_hash)
    if user_id is not None:
        return User.query.get(user_id)
    return None
