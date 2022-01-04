#!/bin/sh
pipenv run alembic upgrade head
pipenv run uvicorn app.asgi:application --reload
