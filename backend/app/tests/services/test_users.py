from faker import Faker

from app.services.users import create_user


def test_create_user(faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    pass


def test_deactivate_user(faker: Faker) -> None:
    """
    Ensure we can deactivate an user.
    """
    pass


def test_load_user() -> None:
    """
    Ensure we can load an user by their ID.
    """
    pass


def test_user_by_email() -> None:
    """
    Ensure we can load an user by their email.
    """
    pass