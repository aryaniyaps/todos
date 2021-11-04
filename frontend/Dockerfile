FROM node:14-alpine as development

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
COPY ./ ${APP_HOME}

# production stage
FROM development as production

# create optimized build
RUN yarn build