from sanic import Sanic, Blueprint
from marshmallow import ValidationError

from app import settings


def create_app(testing: bool = False) -> Sanic:
    """
    Initializes an app instance.

    :param testing: Whether the app is going 
        to be used for testing.

    :return: The created app.
    """
    app = Sanic(__name__)
    if testing:
        app.test_mode = True
    app.update_config(settings)
    register_error_handlers(app)
    register_middleware(app)
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


def register_middleware(app: Sanic) -> None:
    """
    Registers middleware for the app.

    :param app: The app instance.
    """
    from app.middleware.security import security_middleware

    app.register_middleware(
        middleware=security_middleware, 
        attach_to="response"
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
