from flask import Flask
from marshmallow import ValidationError

from app.extensions import cors, db, migrate, mail, login_manager
from app.handlers.validation_error import handle_validation_error
from app.routes.auth import auth_blueprint
from app.routes.users import user_blueprint
from app.routes.todos import todo_blueprint
from app.services.users import load_user


__all__ = ("create_app",)


def create_app(config: str = "app.settings") -> Flask:
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

    :param app: the app instance.
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

    :param app: the app instance.
    """
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(todo_blueprint)


def register_error_handlers(app: Flask) -> None:
    """
    Registers error handlers for the app.

    :param app: the app instance.
    """
    app.register_error_handler(
        ValidationError, 
        handle_validation_error,
    )


application = create_app()
