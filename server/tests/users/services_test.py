from passlib.hash import bcrypt
from pytest import raises

from app.errors import InvalidInput
from app.users.entities import User
from app.users.services import user_service


def test_create_user() -> None:
    """
    Ensure we can create an user.
    """
    email = "user@example.org"
    password = "password"
    result = user_service.create_user(
        email=email,
        password=password
    )
    assert result.email == email
    assert result.password != password
    assert bcrypt.identify(result.password)


def test_create_duplicate_user(user: User) -> None:
    """
    Ensure we cannot create an user with a duplicate email.
    """
    with raises(InvalidInput):
        user_service.create_user(
            email=user.email,
            password="password"
        )
