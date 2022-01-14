from celery import Celery

from app.core.config import CELERY_BROKER_URL


def create_worker() -> Celery:
    """
    Initializes a worker instance.

    :return: The created worker.
    """
    celery = Celery(__name__)
    celery.autodiscover_tasks()
    celery.conf.update(
        broker_url=CELERY_BROKER_URL,
    )
    return celery


worker = create_worker()
