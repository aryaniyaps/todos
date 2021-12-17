from factory import Sequence, Factory, SubFactory, PostGenerationMethodCall

from app.models.todos import Todo
from app.models.users import User


class UserFactory(Factory):
    email = Sequence(lambda n: f"user-{n}@example.org")
    password = PostGenerationMethodCall("set_password", password="avocados")

    class Meta:
        model = User


class TodoFactory(Factory):
    content = "sample content"
    user = SubFactory(UserFactory)

    class Meta:
        model = Todo