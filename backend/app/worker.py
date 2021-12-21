from celery import Celery

from app import config


def create_worker() -> Celery:
    """
    Initializes a worker instance.

    :return: The created worker.
    """
    celery = Celery(
        main=__name__, 
        include=("app.tasks",)
    )
    celery.config_from_object(config)
    return celery


worker = create_worker()