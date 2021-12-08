#!/bin/sh
pipenv run alembic upgrade head
pipenv run uvicorn app:application
