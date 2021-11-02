from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import settings
from backend.routes.auth import auth_router
from backend.routes.users import user_router
from backend.routes.todos import todo_router


__all__ = ("app",)


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = FastAPI(debug=settings.DEBUG)
    register_middleware(app)
    register_routes(app)
    return app


def register_middleware(app: FastAPI) -> None:
    """
    Registers middleware for the app.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_headers=["*"],
    )

def register_routes(app: FastAPI) -> None:
    """
    Registers routes for the app.
    """
    app.include_router(router=auth_router)
    app.include_router(router=user_router)
    app.include_router(router=todo_router)


app = create_app()
