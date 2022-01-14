from flask import Flask

from app.core.config import DEBUG, TESTING


def create_app() -> Flask:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=DEBUG, 
        APPLICATION_ROOT="/api",
        TESTING=TESTING,
    )
    register_routes(app)
    register_event_handlers(app)
    register_middleware(app)
    return app


def register_routes(app: Flask) -> None:
    """
    Registers routes for the app.

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


def register_middleware(app: Flask) -> None:
    """
    Registers middleware for the app.

    :param app: The app instance.
    """
    pass

def register_event_handlers(app: Flask) -> None:
    """
    Registers event handlers for the app.

    :param app: The app instance.
    """
    from app.metrics.handlers import start_metrics

    app.before_first_request(start_metrics)
