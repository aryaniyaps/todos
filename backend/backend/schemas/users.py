from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(
        dump_only=True,
        metadata={
            "description": """
            The ID of the user.
            """
        }
    )

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
        load_only=True,
        metadata={
            "description": """
            The password of the user.
            """
        }
    )

    is_active = fields.Boolean(
        dump_only=True,
        metadata={
            "description": """
            Whether the user is active.
            """
        }
    )

    created_at = fields.DateTime(
        dump_only=True,
        metadata={
            "description": """
            When the user was created.
            """
        }
    )

    updated_at = fields.DateTime(
        dump_only=True,
        metadata={
            "description": """
            When the user was updated.
            """
        }
    )