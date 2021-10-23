#!/bin/bash
flask db migrate
pipenv run gunicorn todos -b 0.0.0.0:8080
