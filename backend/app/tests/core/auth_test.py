from app.models.users import User
from app.core.auth import (
    create_auth_token,
    remove_auth_token,
    check_auth_token
)


def test_create_auth_token(user: User) -> None:
    """
    Ensure we can create an auth token.
    """
    pass


def test_remove_auth_token() -> None:
    """
    Ensure we can remove an auth token.
    """
    pass


def test_check_auth_token() -> None:
    """
    Ensure we can verify an auth token.
    """
    pass