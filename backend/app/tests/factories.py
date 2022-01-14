from factory import Factory, PostGenerationMethodCall, Sequence, SubFactory

from app.todos.entities import Todo
from app.users.entities import User


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
