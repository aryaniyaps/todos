from sanic import Sanic
from marshmallow import ValidationError

from app.handlers.validation_error import handle_validation_error
from app.routes import app_blueprint


def create_app(config: str = "app.settings") -> Sanic:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Sanic(__name__)
    app.update_config(config)
    register_error_handlers(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Sanic) -> None:
    """
    Registers blueprints for the app.

    :param app: The app instance.
    """
    app.blueprint(blueprint=app_blueprint)


def register_error_handlers(app: Sanic) -> None:
    """
    Registers error handlers for the app.

    :param app: The app instance.
    """
    app.register_error_handler(
        ValidationError, 
        handle_validation_error,
    )


application = create_app()
