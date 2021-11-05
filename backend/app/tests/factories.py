from factory import Faker, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from app.extensions import db
from app.models.todos import Todo
from app.models.users import User


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        session = db.session


class UserFactory(BaseFactory):
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = Faker("password", length=12)

    class Meta:
        model = User


class TodoFactory(BaseFactory):
    content = Faker("text", max_nb_chars=250)

    class Meta:
        model = Todo