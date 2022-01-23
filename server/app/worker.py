from celery import Celery

from app.config import CELERY_BROKER_URL


def create_worker() -> Celery:
    """
    Initializes a worker instance.

    :return: The created worker.
    """
    celery = Celery(__name__)
    celery.conf.update(broker_url=CELERY_BROKER_URL)
    celery.autodiscover_tasks()
    return celery


worker = create_worker()
