from marshmallow import Schema
from marshmallow.fields import Boolean, DateTime, Integer, String
from marshmallow.validate import Length


class TodoCreateSchema(Schema):
    content = String(
        required=True, 
        validate=(
            Length(max=250),
        ),
    )


class TodoUpdateSchema(Schema):
    content = String(
        validate=(
            Length(max=250),
        ),
    )
    completed = Boolean()


class TodoSchema(Schema):
    id = Integer(dump_only=True)
    completed: Boolean(dump_default=False)
    content: String(required=True)
    created_at = DateTime(dump_only=True)
    updated_at = DateTime(dump_only=True)


todo_create_schema = TodoCreateSchema()

todo_update_schema = TodoUpdateSchema()

todo_schema = TodoSchema()

todos_schema = TodoSchema(many=True)