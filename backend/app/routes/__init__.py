from flask import Blueprint

from .auth import auth_blueprint
from .todos import todo_blueprint
from .users import user_blueprint


__all__ = ("app_blueprint",)


app_blueprint = Blueprint("app", __name__, url_prefix="/api")

app_blueprint.register_blueprint(auth_blueprint)
app_blueprint.register_blueprint(todo_blueprint)
app_blueprint.register_blueprint(user_blueprint)