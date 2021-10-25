FROM node:17-alpine

# set workdir
ARG APP_HOME=/frontend/
WORKDIR ${APP_HOME}

# copy dep files
COPY package-lock.json ./package.json ${APP_HOME}

# install dependencies
RUN npm install

# copy project files
COPY .. ${APP_HOME}