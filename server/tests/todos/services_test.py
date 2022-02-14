from pytest import raises

from app.errors import ResourceNotFound
from app.todos.entities import Todo
from app.todos.services import TodoService
from app.users.entities import User


def test_get_todos(user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    results = TodoService.get_todos(user_id=user.id)
    assert results


def test_get_todo(todo: Todo) -> None:
    """
    Ensure we can get a todo.
    """
    result = TodoService.get_todo(
        todo_id=todo.id, 
        user_id=todo.user_id,
    )
    assert result == todo


def test_get_foreign_todo(user: User, foreign_todo: Todo) -> None:
    """
    Ensure we cannot get a todo
    owned by another user.
    """
    with raises(ResourceNotFound):
        TodoService.get_todo(
            todo_id=foreign_todo.id,
            user_id=user.id,
        )
        

def test_create_todo(user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "content"
    result = TodoService.create_todo(
        content=content,
        user_id=user.id,
    )
    assert result.content == content
    assert result.user_id == user.id
    assert not result.completed


def test_update_todo(todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    content = "content"
    result = TodoService.update_todo(
        user_id=todo.user_id,
        todo_id=todo.id, 
        completed=True, 
        content=content,
    )
    assert result.content == content
    assert result.completed


def test_update_foreign_todo(user: User, foreign_todo: Todo) -> None:
    """
    Ensure we cannot update a todo
    owned by another user.
    """
    with raises(ResourceNotFound):
        TodoService.update_todo(
            user_id=user.id,
            todo_id=foreign_todo.id,
            completed=True,
        )


def test_delete_todo(todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    TodoService.delete_todo(
        user_id=todo.user_id, 
        todo_id=todo.id,
    )
    with raises(ResourceNotFound):
        TodoService.get_todo(
            user_id=todo.user_id,
            todo_id=todo.id,
        )


def test_delete_foreign_todo(user: User, foreign_todo: Todo) -> None:
    """
    Ensure we cannot delete a todo
    owned by another user.
    """
    with raises(ResourceNotFound):
        TodoService.delete_todo(
            user_id=user.id,
            todo_id=foreign_todo.id,
        )


def test_clear_todos(user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    TodoService.clear_todos(user_id=user.id)
    assert not user.todos
