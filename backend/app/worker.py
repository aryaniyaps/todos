from celery import Celery

from app.conf import settings


def create_worker() -> Celery:
    """
    Initializes a worker instance.

    :return: The created worker.
    """
    celery = Celery(main=__name__, include=("app.tasks",))
    celery.conf.update(
        broker_url=settings.CELERY_BROKER_URL,
        result_expires=settings.CELERY_RESULT_EXPIRES,
        result_backend=settings.CELERY_RESULT_BACKEND,
    )
    return celery


worker = create_worker()
