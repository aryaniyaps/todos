#!/bin/bash
pipenv run flask db upgrade
pipenv run flask run -h 0.0.0.0 -p 8000
