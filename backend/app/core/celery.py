from celery import Celery, Task
from flask import Flask

from app import application


def create_celery_app(app: Flask) -> Celery:
    """
    Initializes a Celery app instance.

    :param app: The Flask app instance.

    :return: The created app.
    """
    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super().__call__(*args, **kwargs)

    celery_app = Celery(
        main=app.import_name, 
        task_cls=ContextTask, 
        include=("app.tasks",)
    )
    celery_app.conf.update(app.config)
    return celery_app


celery = create_celery_app(application)