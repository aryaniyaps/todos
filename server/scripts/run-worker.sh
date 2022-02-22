#!/bin/sh
pipenv run celery -A app.worker.worker worker