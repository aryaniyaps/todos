from faker import Faker

from app.models.users import User


def test_set_password(test_user: User, faker: Faker):
    """
    Ensure we can set a password on a user.
    """
    pass


def test_check_password(test_user: User, faker: Faker):
    """
    Ensure we can verify an user's password.
    """
    pass