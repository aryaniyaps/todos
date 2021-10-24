FROM python:3.9-slim

# set workdir
ARG APP_HOME=/app/
WORKDIR ${APP_HOME}

# install pipenv
RUN pip install pipenv

# install dependencies
COPY ./Pipfile.lock ./Pipfile ${APP_HOME}
RUN pipenv install --deploy

# copy project files
COPY ./ ${APP_HOME}
