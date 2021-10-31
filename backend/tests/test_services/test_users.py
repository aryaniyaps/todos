import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.users import create_user, deactivate_user


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession) -> None:
    """
    Ensure we can create an user.
    """
    user = await create_user(
        session=session,
        email="alpha@abc.com",
        username="alpha",
        password="password"
    )
    assert user.is_active
    assert user.check_password("password")
    assert user.username == "alpha"
    assert user.email == "alpha@abc.com"


@pytest.mark.asyncio
async def test_deactivate_user(session: AsyncSession) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = await create_user(
        session=session,
        email="alpha@abc.com",
        username="alpha",
        password="password"
    )
    await deactivate_user(session=session, user=user)
    assert not user.is_active