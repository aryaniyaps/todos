from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import settings


__all__ = ("app",)


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    app = FastAPI(debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_headers=["*"]
    )
    return app


app = create_app()
