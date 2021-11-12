#!/bin/sh
pipenv run flask db upgrade
pipenv run gunicorn app
