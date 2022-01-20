from flask import Flask

from app.core.config import DEBUG, TESTING, SECRET_KEY


def create_app() -> Flask:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=DEBUG, 
        SECRET_KEY=SECRET_KEY,
        APPLICATION_ROOT="/api",
        TESTING=TESTING,
    )
    configure_routes(app)
    configure_extensions(app)
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

    @app.get("/status")
    def check_status():
        """
        Check the app's status.
        """
        return {"running": True}

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

def configure_event_handlers(app: Flask) -> None:
    """
    Configures event handlers for the app.

    :param app: The app instance.
    """
    from app.core.database import teardown_session

    app.teardown_appcontext(teardown_session)
