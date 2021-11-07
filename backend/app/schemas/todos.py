from marshmallow import Schema, fields

__all__ = ("todo_schema", "todos_schema")


class TodoSchema(Schema):
    id = fields.Integer(
        dump_only=True,
        metadata={
            "description": """
            The ID of the todo.
            """
        }
    )

    content = fields.String(
        required=True,
        metadata={
            "description": """
            The content of the todo.
            """
        }
    )

    completed = fields.Boolean(
        dump_only=True,
        metadata={
            "description": """
            Whether the todo is completed.
            """
        }
    )

    created_at = fields.DateTime(
        dump_only=True,
        metadata={
            "description": """
            When the todo was created.
            """
        }
    )

    updated_at = fields.DateTime(
        dump_only=True,
        metadata={
            "description": """
            When the todo was updated.
            """
        }
    )

todo_schema = TodoSchema()

todos_schema = TodoSchema(many=True)