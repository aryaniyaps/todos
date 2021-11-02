from schematics import Model
from schematics.types import StringType


class TodoSerializer(Model):
    content = StringType(
        required=True,
        metadata={
            "description": """
            The content of the todo.
            """
        }
    )