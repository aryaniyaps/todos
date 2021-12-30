from passlib.hash import argon2

from app.models.users import User


def test_set_password(user: User) -> None:
    """
    Ensure we can set a password on a user.
    """
    user.set_password(password="avocados")
    assert user.password != "avocados"
    assert user.check_password(password="avocados")
    assert argon2.identify(user.password)


def test_check_password(user: User) -> None:
    """
    Ensure we can verify an user's password.
    """
    user.set_password(password="avocados")
    assert not user.check_password(password="bananas")
    assert user.check_password(password="avocados")
