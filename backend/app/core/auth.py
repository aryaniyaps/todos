from binascii import hexlify
from os import urandom
from typing import Optional

from flask_httpauth import HTTPTokenAuth

from app.models.users import User


auth = HTTPTokenAuth()


def generate_auth_token(length: int = 20) -> str:
    """
    Generates an authentication token.

    :param length: The length of the auth token.
    :return: The generated auth token.
    """
    return hexlify(urandom(length)).decode()


@auth.verify_token
def check_auth_token(token: Optional[str]) -> Optional[User]:
    """
    Checks and gets the user associated with the
    given auth token, if they exist.

    :param token: The auth token to check.
    
    :return: The user associated with the auth token.
    """
    if token is not None:
        return User.query.filter_by(auth_token=token).first()
    return None
