from celery import Celery, Task
from flask import Flask

from app import application


def create_celery(app: Flask) -> Celery:
    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super().__call__(*args, **kwargs)

    celery = Celery(app.import_name, task_cls=ContextTask)
    celery.conf.update(app.config)
    return celery

celery = create_celery(application)