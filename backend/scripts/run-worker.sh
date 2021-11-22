#!/bin/sh
pipenv run celery -A app.core.celery worker