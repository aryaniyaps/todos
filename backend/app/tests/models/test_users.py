from faker import Faker
from passlib.hash import argon2

from app.models.users import User


def test_set_password(user: User, faker: Faker) -> None:
    """
    Ensure we can set a password on a user.
    """
    password = faker.password(length=12)
    user.set_password(password=password)
    assert argon2.identify(user.password)
    assert user.check_password(password=password)


def test_check_password(user: User, faker: Faker) -> None:
    """
    Ensure we can verify an user's password.
    """
    password = faker.password(length=12)
    user.set_password(password=password)
    assert user.check_password(password=password)


def test_check_wrong_password(user: User, faker: Faker) -> None:
    """
    Ensure we cannot verify a wrong password.
    """
    pass