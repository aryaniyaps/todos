from fastapi import FastAPI

from backend import settings


__all__ = ("app",)


def create_app() -> FastAPI:
    """
    Initializes an app instance.

    :return: The created app.
    """
    return FastAPI(debug=settings.DEBUG)


app = create_app()
