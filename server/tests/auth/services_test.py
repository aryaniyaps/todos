from pytest import raises

from app.auth.services import auth_service
from app.errors import InvalidInput
from app.users.entities import User


def test_authenticate(user: User) -> None:
    """
    Ensure we can authenticate an user.
    """
    result = auth_service.authenticate(
        email=user.email,
        password="password"
    )
    assert result == user


def test_authenticate_invalid(user: User) -> None:
    """
    Ensure we cannot authenticate an user
    with invalid credentials.
    """
    with raises(InvalidInput):
        auth_service.authenticate(
            email=user.email,
            password="invalid-password"
        )