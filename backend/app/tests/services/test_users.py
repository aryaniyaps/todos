from faker import Faker
from sqlalchemy.orm import Session

from app.services.users import create_user, deactivate_user


def test_create_user(session: Session, faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    email = faker.ascii_safe_email()
    password = faker.password(length=12)
    user = create_user(
        session=session,
        email=email,
        password=password
    )
    assert user.is_active
    assert user.check_password(password)
    assert user.email == email


def test_deactivate_user(session: Session, faker: Faker) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = create_user(
        session=session,
        email=faker.ascii_safe_email(),
        password=faker.password(length=12)
    )
    deactivate_user(session=session, user=user)
    assert not user.is_active