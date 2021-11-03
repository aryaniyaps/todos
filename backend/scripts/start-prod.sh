#!/bin/sh
pipenv run flask db upgrade
pipenv run gunicorn app -b 0.0.0.0:8000
