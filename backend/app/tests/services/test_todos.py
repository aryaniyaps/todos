from faker import Faker
from sqlalchemy.orm import Session

from app.services.todos import create_todo


def test_create_todo(session: Session, faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    content = faker.text(250)
    todo = create_todo(
        session=session,
        content=content,
        user_id=None
    )
    assert todo.content == content


def test_update_todo(session: Session, faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    pass


def test_delete_todo(session: Session) -> None:
    """
    Ensure we can delete a todo.
    """
    pass