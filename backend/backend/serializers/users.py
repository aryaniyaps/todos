from schematics import Model
from schematics.types import EmailType, StringType


class UserSerializer(Model):
    email = EmailType(
        required=True,
        metadata={
            "description": """
            The email of the user.
            """
        }
    )

    password = StringType(
        required=True,
        metadata={
            "description": """
            The password of the user.
            """
        }
    )