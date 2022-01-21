# build stage
FROM python:3.9-slim as build

# set workdir
ARG APP_HOME=/backend/
WORKDIR ${APP_HOME}

# install pipenv
RUN pip install --no-cache pipenv

# copy dep files
COPY Pipfile.lock ./Pipfile ${APP_HOME}

# development stage
FROM build as development

# install dependencies
RUN pipenv install --dev

# copy project files
COPY ./ ${APP_HOME}

# production stage
FROM build as production

# install dependencies
RUN pipenv install --deploy

# copy project files
COPY ./ ${APP_HOME}
