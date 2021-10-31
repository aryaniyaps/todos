from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.users import User


async def create_user(
    session: AsyncSession,
    email: str, 
    username: str, 
    password: str,
) -> User:
    """
    Creates an user instance.
    """
    user = User(email=email, username=username)
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
