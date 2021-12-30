from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import DEBUG


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = FastAPI(
        title="Todos",
        root_path="/api",
        debug=DEBUG,
    )
    register_routes(app)
    register_middleware(app)
    return app


def register_routes(app: FastAPI) -> None:
    """
    Registers routes for the app.

    :param app: The app instance.
    """
    from app.api.routes.auth import auth_router
    from app.api.routes.todos import todo_router
    from app.api.routes.users import user_router

    @app.get("/status", name="status")
    def check_status():
        """
        Check the app's status.
        """
        return {"running": True}

    app.include_router(auth_router)
    app.include_router(todo_router)
    app.include_router(user_router)


def register_middleware(app: FastAPI) -> None:
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


application = create_app()
