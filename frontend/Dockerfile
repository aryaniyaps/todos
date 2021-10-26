FROM node:17-alpine

# set workdir
ARG APP_HOME=/frontend/
WORKDIR ${APP_HOME}

# install yarn
RUN npm install yarn

# copy dep files
COPY yarn.lock ./package.json ${APP_HOME}

# install dependencies
RUN yarn install

# copy project files
COPY .. ${APP_HOME}