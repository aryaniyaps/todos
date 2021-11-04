from faker import Faker

from app.services.users import create_user, deactivate_user


def test_create_user(faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    email = faker.ascii_safe_email()
    password = faker.password(length=12)
    user = create_user(
        email=email,
        password=password
    )
    assert user.is_active
    assert user.check_password(password)
    assert user.email == email


def test_deactivate_user(faker: Faker) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = create_user(
        email=faker.ascii_safe_email(),
        password=faker.password(length=12)
    )
    deactivate_user(user=user)
    assert not user.is_active


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