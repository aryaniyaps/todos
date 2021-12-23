from celery import Celery

from app.config import (
    CELERY_BROKER_URL, 
    CELERY_RESULT_BACKEND, 
    CELERY_RESULT_EXPIRES
)


def create_worker() -> Celery:
    """
    Initializes a worker instance.

    :return: The created worker.
    """
    celery = Celery(
        main=__name__, 
        include=("app.tasks",)
    )
    celery.conf.update(
        broker_url=CELERY_BROKER_URL,
        result_expires=CELERY_RESULT_EXPIRES,
        result_backend=CELERY_RESULT_BACKEND,
    )
    return celery


worker = create_worker()