#!/bin/sh
pipenv run alembic upgrade head
pipenv run gunicorn app.wsgi
