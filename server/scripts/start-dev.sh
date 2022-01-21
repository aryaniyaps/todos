#!/bin/sh
pipenv run alembic upgrade head
pipenv run flask run -h 0.0.0.0 -p 8000
