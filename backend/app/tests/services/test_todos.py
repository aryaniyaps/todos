from faker import Faker

from app.services.todos import create_todo


def test_create_todo(faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    content = faker.text(250)
    todo = create_todo(
        content=content,
        user_id=None
    )
    assert todo.content == content


def test_update_todo(faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    pass


def test_delete_todo() -> None:
    """
    Ensure we can delete a todo.
    """
    pass