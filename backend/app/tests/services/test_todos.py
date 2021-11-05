from faker import Faker

from app.models.users import User
from app.models.todos import Todo
from app.services.todos import create_todo, update_todo, delete_todo


def test_create_todo(test_user: User, faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    content = faker.text(250)
    todo = create_todo(
        content=content,
        user_id=test_user.id
    )
    assert todo.content == content
    assert todo.user_id == test_user.id
    assert not todo.completed


def test_update_todo(test_todo: Todo, faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    content = faker.text(250)
    todo = update_todo(
        todo=test_todo,
        content=content,
        completed=True
    )
    assert todo.content == content
    assert todo.completed


def test_delete_todo(test_todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    delete_todo(todo=test_todo)
    print(test_todo)