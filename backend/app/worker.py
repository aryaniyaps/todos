from celery import Celery

from app import settings


def create_celery() -> Celery:
    """
    Initializes a Celery app instance.

    :param app: The central app instance.

    :return: The created app.
    """

    celery_app = Celery(
        main=__name__, 
        include=("app.tasks",)
    )
    celery_app.conf.update(settings)
    return celery_app


celery = create_celery()