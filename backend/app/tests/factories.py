from factory import Faker, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from app.extensions import db
from app.models.todos import Todo
from app.models.users import User


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"


class UserFactory(BaseFactory):
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = Faker("password", length=12)

    class Meta:
        model = User


class TodoFactory(BaseFactory):
    content = Faker("text", max_nb_chars=250)
    user = SubFactory(UserFactory)

    class Meta:
        model = Todo