from flask import Flask
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> Flask:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = Flask(__name__)
    register_routes(app)
    register_event_handlers(app)
    register_middleware(app)
    return app


def register_routes(app: Flask) -> None:
    """
    Registers routes for the app.

    :param app: The app instance.
    """
    from app.routes.auth import auth_blueprint
    from app.routes.todos import todo_blueprint
    from app.routes.users import user_blueprint

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
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def register_event_handlers(app: Flask) -> None:
    """
    Registers event handlers for the app.

    :param app: The app instance.
    """
    from app.handlers.metrics import start_metrics

    app.add_event_handler(
        event_type="startup",
        func=start_metrics
    )
