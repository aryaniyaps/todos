from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Email(
        required=True,
        metadata={
            "description": """
            The email of the user.
            """
        }
    )

    password = fields.String(
        required=True,
        metadata={
            "description": """
            The password of the user.
            """
        }
    )