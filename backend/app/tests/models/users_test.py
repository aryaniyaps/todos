from passlib.hash import argon2

from app.models.users import User


def test_set_password(user: User) -> None:
    """
    Ensure we can set a password on a user.
    """
    user.set_password(password="password")
    assert user.password != "password"
    assert user.check_password(password="password")
    assert argon2.identify(user.password)


def test_check_password(user: User) -> None:
    """
    Ensure we can verify an user's password.
    """
    user.set_password(password="password")
    assert not user.check_password(password="bananas")
    assert user.check_password(password="password")