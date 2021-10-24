FROM python:3.9-slim as builder

# set workdir
ARG APP_HOME=/app/
WORKDIR ${APP_HOME}

FROM builder as production

RUN pip install --no-cache pipenv

# copy dep files
COPY ./Pipfile.lock ./Pipfile ${APP_HOME}

# install dependencies
RUN pipenv install --deploy

# copy project files
COPY ./ ${APP_HOME}

FROM builder as development

RUN pip install pipenv

# copy dep files
COPY ./Pipfile.lock ./Pipfile ${APP_HOME}

# install dependencies
RUN pipenv install --dev

# copy project files
COPY ./ ${APP_HOME}
