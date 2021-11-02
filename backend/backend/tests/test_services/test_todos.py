import pytest
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.todos import create_todo


@pytest.mark.asyncio
async def test_create_todo(session: AsyncSession, faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    content = faker.password(length=12)
    todo = await create_todo(
        session=session,
        content=content,
        user_id=None
    )
    assert todo.content == content


@pytest.mark.asyncio
async def test_update_todo(session: AsyncSession, faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    pass


@pytest.mark.asyncio
async def test_delete_todo(session: AsyncSession) -> None:
    """
    Ensure we can delete a todo.
    """
    pass