from flask import Blueprint

from .auth import auth_blueprint
from .todos import todo_blueprint
from .users import user_blueprint


__all__ = ("api_blueprint",)


api_blueprint = Blueprint(
    name="api",
    import_name=__name__,
    url_prefix="/api"
)

api_blueprint.register_blueprint(auth_blueprint)
api_blueprint.register_blueprint(todo_blueprint)
api_blueprint.register_blueprint(user_blueprint)