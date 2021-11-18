# Todos app

[![GitHub](https://img.shields.io/github/license/aryaniyaps/todos)](https://github.com/aryaniyaps/todos)
[![codecov](https://codecov.io/gh/aryaniyaps/todos/branch/main/graph/badge.svg?token=K82QAJ2EF7)](https://codecov.io/gh/aryaniyaps/todos)

This is an example todos app.

## Tech stack used

| library / service                                      | description                  |
| ------------------------------------------------------ | ---------------------------- |
| [React](https://github.com/facebook/react)             | UI library                   |
| [Storybook](https://github.com/storybookjs/storybook)  | UI component explorer        |
| [Webpack](https://github.com/webpack/webpack)          | Module bundler               |
| [Nginx](https://github.com/nginx/nginx)                | web server                   |
| [HAProxy](https://github.com/haproxy/haproxy)          | reverse proxy/ load balancer |
| [Flask](https://github.com/pallets/flask)              | web framework                |
| [Gunicorn](https://github.com/benoitc/gunicorn)        | WSGI HTTP server             |
| [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) | mapper/ SQL toolkit          |
| [Alembic](https://github.com/sqlalchemy/alembic)       | migrations tool              |
| [MySQL](https://github.com/mysql/mysql-server)         | database server              |
| [Pytest](https://github.com/pytest-dev/pytest)         | testing framework            |

## How to use

You can use [Docker Compose](https://github.com/docker/compose) to run this application.
Make sure you have it installed on your machine! For development purposes, you can get
going with the following command:

```text
docker compose up --build
```

This spins up a few containers locally. The site will be available at
http://localhost. To use in a production environment, you need to set environment
variables first. Here's an [example env file](example.env) to reference.

```text
docker compose -f docker-compose.yml up -d
```
