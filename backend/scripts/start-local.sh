#!/bin/sh
pipenv run alembic upgrade head
pipenv run uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
