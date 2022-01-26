from marshmallow import Schema
from marshmallow.fields import DateTime, Email, Integer, String
from marshmallow.validate import Length


class UserCreateSchema(Schema):
    email = Email(required=True)
    password = String(
        required=True, 
        load_only=True, 
        validate=(
            Length(min=8, max=255)
        ),
    )


class UserSchema(Schema):
    id = Integer(dump_only=True)
    email = Email(required=True)
    created_at = DateTime(dump_only=True)
    updated_at = DateTime(dump_only=True)


user_create_schema = UserCreateSchema()

user_schema = UserSchema()
