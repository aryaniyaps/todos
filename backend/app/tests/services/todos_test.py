from app.models.todos import Todo
from app.models.users import User
from app.services.todos import (
    create_todo, 
    delete_todo, 
    update_todo,
    clear_todos
)


def test_create_todo(user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "sample content"
    todo = create_todo(
        content=content,
        user_id=user.id
    )
    assert todo.content == content
    assert todo.user_id == user.id
    assert not todo.completed


def test_update_todo(todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    content = "sample content"
    todo = update_todo(
        todo=todo,
        content=content,
        completed=True
    )
    assert todo.content == content
    assert todo.completed


def test_delete_todo(todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    delete_todo(todo=todo)
    assert not Todo.query.get(todo.id)


def test_clear_todos(user: User) -> None:
    """
    Ensure we can clear todos for an user.
    """
    clear_todos(user=user)
    todos = Todo.query.filter_by(user_id=user.id)
    assert not todos.first()