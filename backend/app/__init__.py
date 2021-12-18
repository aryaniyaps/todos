from fastapi import FastAPI

from app import settings


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = FastAPI(debug=settings.DEBUG)
    register_middleware(app)
    register_blueprints(app)
    return app


def register_blueprints(app: FastAPI) -> None:
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


def register_middleware(app: FastAPI) -> None:
    """
    Registers middleware for the app.

    :param app: The app instance.
    """
    from app.middleware.security import security_middleware

    app.register_middleware(
        middleware=security_middleware, 
        attach_to="response"
    )


application = create_app()
