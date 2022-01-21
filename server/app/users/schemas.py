from marshmallow import Schema
from marshmallow.fields import DateTime, Email, Integer, String


class UserCreateSchema(Schema):
    email = Email(required=True)
    password = String(required=True, load_only=True)


class UserSchema(Schema):
    id = Integer(dump_only=True)
    email = Email(required=True)
    created_at = DateTime(dump_only=True)
    updated_at = DateTime(dump_only=True)


user_create_schema = UserCreateSchema()

user_schema = UserSchema()
