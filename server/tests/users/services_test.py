from passlib.hash import bcrypt
from pytest import raises

from app.errors import InvalidInput
from app.users.entities import User
from app.users.services import user_service


def test_get_user_by_email(user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    result = user_service.user_by_email(email=user.email)
    assert result == user


def test_get_user_by_id(user: User) -> None:
    """
    Ensure we can get an user by ID.
    """
    result = user_service.get_user(user_id=user.id)
    assert result == user


def test_create_user() -> None:
    """
    Ensure we can create an user.
    """
    result = user_service.create_user(
        email="user@example.com",
        password="password"
    )
    assert result.email == "user@example.com"
    assert result.password != "password"
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
