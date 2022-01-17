from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from app.core.database import db_session
from app.todos.entities import Todo
from app.users.entities import User


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db_session
        sqlalchemy_session_persistence = "commit"
        abstract = True


class UserFactory(BaseFactory):
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = PostGenerationMethodCall("set_password", password="password")

    class Meta:
        model = User


class TodoFactory(BaseFactory):
    content = "sample content"
    user = SubFactory(UserFactory)

    class Meta:
        model = Todo
