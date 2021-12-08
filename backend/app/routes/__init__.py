from sanic import Blueprint

from .auth import auth_blueprint
from .todos import todo_blueprint
from .users import user_blueprint


__all__ = ("app_blueprint",)


app_blueprint = Blueprint.group(
    auth_blueprint, 
    todo_blueprint, 
    user_blueprint, 
    url_prefix="/api"
)