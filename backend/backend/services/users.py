from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.users import User


async def user_by_email(session: AsyncSession, email: str) -> Optional[User]:
    """
    Gets an user by their email.
    """
    query = select(User).filter(User.email == email)
    return (await session.execute(query)).scalar_one()


async def create_user(
    session: AsyncSession,
    email: str, 
    password: str,
) -> User:
    """
    Creates a new user.
    """
    user = User(email=email)
    user.set_password(password=password)
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user


async def deactivate_user(session: AsyncSession, user: User) -> User:
    """
    Deactivates the given user.
    """
    user.is_active = False
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user
