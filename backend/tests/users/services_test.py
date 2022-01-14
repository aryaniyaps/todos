from passlib.hash import argon2

from app.users.entities import User
from app.users.services import UserService


def test_user_by_email(user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    result = UserService().user_by_email(email=user.email)
    assert result == user


def test_create_user() -> None:
    """
    Ensure we can create an user.
    """
    email = "tester@abc.com"
    password = "avocados"
    result = UserService().create_user(
        email=email,
        password=password
    )
    assert result.email == email
    assert result.password != password
    assert result.check_password(password)
    assert argon2.identify(result.password)
