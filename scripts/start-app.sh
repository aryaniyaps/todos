#!/bin/bash
pipenv run flask db upgrade
pipenv run gunicorn todos -b 0.0.0.0:8000
