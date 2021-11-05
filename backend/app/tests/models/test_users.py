from faker import Faker
from passlib.hash import argon2

from app.models.users import User


def test_set_password(test_user: User, faker: Faker):
    """
    Ensure we can set a password on a user.
    """
    password = faker.password(length=12)
    test_user.set_password(password=password)
    assert argon2.identity(test_user.password)


def test_check_password(test_user: User, faker: Faker):
    """
    Ensure we can verify an user's password.
    """
    password = faker.password(length=12)
    test_user.set_password(password=password)
    assert test_user.check_password(password=password)