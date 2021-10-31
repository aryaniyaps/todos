from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.todos import Todo


async def create_todo(session: AsyncSession, content: str, user_id: int) -> Todo:
    """
    Creates a new todo.
    """
    todo = Todo(content=content, user_id=user_id)
    session.add(instance=todo)
    await session.commit()
    await session.refresh(instance=todo)
    return todo


async def update_todo(
    session: AsyncSession, 
    todo: Todo, 
    content: Optional[str], 
    completed: Optional[bool],
) -> Todo:
    """
    Updates the given todo.
    """
    if content is not None:
        todo.content = content
    if completed is not None:
        todo.completed = completed
    await session.commit()
    await session.refresh(instance=todo)
    return todo


async def delete_todo(session: AsyncSession, todo: Todo) -> None:
    """
    Deletes the given todo.
    """
    await session.delete(instance=todo)
    await session.commit()