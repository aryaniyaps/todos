from sanic import Sanic, Blueprint
from marshmallow import ValidationError


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
    from app.routes.auth import auth_blueprint
    from app.routes.todos import todo_blueprint
    from app.routes.users import user_blueprint

    app.blueprint(
        Blueprint.group(
            auth_blueprint,
            todo_blueprint,
            user_blueprint,
            url_prefix="/api"
        )
    )


def register_error_handlers(app: Sanic) -> None:
    """
    Registers error handlers for the app.

    :param app: The app instance.
    """
    from app.handlers.validation_error import validation_error_handler

    app.error_handler.add(
        exception=ValidationError,
        handler=validation_error_handler
    )


application = create_app()
