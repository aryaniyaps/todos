from marshmallow import Schema, fields


class TodoSchema(Schema):
    content = fields.String(
        required=True,
        metadata={
            "description": """
            The content of the todo.
            """
        }
    )