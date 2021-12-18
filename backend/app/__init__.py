from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app import settings


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = FastAPI(debug=settings.DEBUG)
    register_routes(app)
    register_middleware(app)
    return app


def register_routes(app: FastAPI) -> None:
    """
    Registers routes for the app.

    :param app: The app instance.
    """
    from app.routes.auth import auth_router
    from app.routes.todos import todo_router
    from app.routes.users import user_router

    app_router = APIRouter(prefix="/api")

    app_router.include_router(auth_router)
    app_router.include_router(todo_router)
    app_router.include_router(user_router)
    app.include_router(app_router)


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
