from factory import Faker, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from app.extensions import db
from app.models.todos import Todo
from app.models.users import User


class BaseFactory(SQLAlchemyModelFactory):
    """
    Base factory that all factories must subclass.
    """
    class Meta:
        abstract = True
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """
    User factory.
    """
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = "password"

    class Meta:
        model = User


class TodoFactory(BaseFactory):
    """
    Todo factory.
    """
    content = "sample content"
    completed = False
    user = SubFactory(UserFactory)

    class Meta:
        model = Todo