import pytest
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.users import create_user, deactivate_user


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    email = faker.ascii_safe_email()
    password = faker.password(length=12)
    user = await create_user(
        session=session,
        email=email,
        password=password
    )
    assert user.is_active
    assert user.check_password(password)
    assert user.email == email


@pytest.mark.asyncio
async def test_deactivate_user(session: AsyncSession, faker: Faker) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = await create_user(
        session=session,
        email=faker.ascii_safe_email(),
        password=faker.password(length=12)
    )
    await deactivate_user(session=session, user=user)
    assert not user.is_active