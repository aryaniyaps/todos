from celery import Celery
from sanic import Sanic

from app import application


def create_celery_app(app: Sanic) -> Celery:
    """
    Initializes a Celery app instance.

    :param app: The central app instance.

    :return: The created app.
    """

    celery_app = Celery(
        main=app.name, 
        include=("app.tasks",)
    )
    celery_app.conf.update(app.config)
    return celery_app


celery = create_celery_app(application)