from factory import Sequence, SubFactory, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

from app.models.todos import Todo
from app.models.users import User


class BaseFactory(SQLAlchemyModelFactory):
    """
    Base factory that all factories must subclass.
    """
    class Meta:
        abstract = True


class UserFactory(BaseFactory):
    """
    User factory.
    """
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = PostGenerationMethodCall("set_password", password="password")

    class Meta:
        model = User


class TodoFactory(BaseFactory):
    """
    Todo factory.
    """
    content = "sample content"
    user = SubFactory(UserFactory)

    class Meta:
        model = Todo