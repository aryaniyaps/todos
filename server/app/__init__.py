from flask import Flask

from app.config import DEBUG, TESTING, SECRET_KEY


def create_app() -> Flask:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=DEBUG, 
        SECRET_KEY=SECRET_KEY,
        TESTING=TESTING,
    )
    configure_routes(app)
    configure_extensions(app)
    configure_error_handlers(app)
    configure_event_handlers(app)
    configure_middleware(app)
    return app


def configure_routes(app: Flask) -> None:
    """
    Configures routes for the app.

    :param app: The app instance.
    """
    from app.auth.routes import auth_blueprint
    from app.todos.routes import todo_blueprint
    from app.users.routes import user_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(todo_blueprint)
    app.register_blueprint(user_blueprint)


def configure_extensions(app: Flask) -> None:
    """
    Configures extensions for the app.

    :param app: The app instance.
    """
    from app.extensions import login_manager

    login_manager.init_app(app)


def configure_middleware(app: Flask) -> None:
    """
    Configures middleware for the app.

    :param app: The app instance.
    """
    pass


def configure_error_handlers(app: Flask) -> None:
    """
    Configures error handlers for the app.

    :param app: The app instance.
    """
    from app.errors import InvalidInput, ResourceNotFound
    from app.error_handlers import (
        invalid_input_handler, 
        resource_not_found_handler
    )

    app.register_error_handler(
        InvalidInput, 
        invalid_input_handler,
    )
    app.register_error_handler(
        ResourceNotFound, 
        resource_not_found_handler,
    )

def configure_event_handlers(app: Flask) -> None:
    """
    Configures event handlers for the app.

    :param app: The app instance.
    """
    from app.database.events import shutdown_session

    app.teardown_appcontext(shutdown_session)
