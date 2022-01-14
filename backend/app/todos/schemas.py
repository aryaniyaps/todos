from marshmallow import Schema
from marshmallow.fields import Boolean, DateTime, Integer, String


class TodoCreateSchema(Schema):
    content = String(required=True)


class TodoUpdateSchema(Schema):
    content = String()
    completed = Boolean()


class TodoSchema(Schema):
    id = Integer(dump_only=True)
    completed: Boolean(dump_default=False)
    content: String(required=True)
    created_at = DateTime(dump_only=True)
    updated_at = DateTime(dump_only=True)
