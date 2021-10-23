#!/bin/bash
pipenv run flask db migrate
pipenv run gunicorn todos -b 0.0.0.0:8000
