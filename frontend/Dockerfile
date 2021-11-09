# development stage
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

# build stage
FROM development as build

# create optimized build
RUN yarn build

# production stage
FROM nginx:1.21-alpine as production

# copy configuration files
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

# copy compiled build
COPY --from=build /frontend/build /usr/share/nginx/html