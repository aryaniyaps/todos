from faker import Faker

from app.models.todos import Todo
from app.models.users import User
from app.services.todos import create_todo, delete_todo, update_todo


def test_create_todo(user: User, faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    content = faker.text(250)
    todo = create_todo(
        content=content,
        user_id=user.id
    )
    assert todo.content == content
    assert todo.user_id == user.id
    assert not todo.completed


def test_update_todo(todo: Todo, faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    content = faker.text(250)
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
    result = Todo.query.filter_by(id=todo.id)
    assert result.first() is None