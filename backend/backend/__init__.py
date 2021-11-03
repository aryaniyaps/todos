from flask import Flask
from marshmallow import ValidationError

from backend.services.users import load_user
from backend.handlers.validation_error import handle_validation_error
from backend.extensions import cors, db, migrate, mail, login_manager
from backend.blueprints.auth import auth_blueprint
from backend.blueprints.users import user_blueprint
from backend.blueprints.todos import todo_blueprint


__all__ = ("create_app",)


def create_app(config: str = "backend.settings") -> Flask:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    return app


def register_extensions(app: Flask) -> None:
    """
    Registers extensions for the app.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.user_loader(load_user)


def register_blueprints(app: Flask) -> None:
    """
    Registers blueprints for the app.
    """
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(todo_blueprint)


def register_error_handlers(app: Flask) -> None:
    """
    Registers error handlers for the app.
    """
    app.register_error_handler(
        ValidationError, 
        handle_validation_error,
    )


application = create_app()
