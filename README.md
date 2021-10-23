# Todos app
This is an example todos app, which uses [Python](https://python.org) for the backend.

## Tech stack used
- [Flask](https://github.com/pallets/flask) web framework
- [Nginx](https://github.com/nginx/nginx) reverse proxy
- [Gunicorn](https://github.com/benoitc/gunicorn) WSGI HTTP server
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) mapper/ SQL toolkit
- [Alembic](https://github.com/sqlalchemy/alembic) migrations
- [PostgreSQL](https://github.com/postgres/postgres) database server
- [Redis](https://github.com/redis/redis) cache store

## How to use
You can use [Docker Compose](https://github.com/docker/compose) to run this application. Make sure you
have it installed on your machine! For development purposes, you can get going with the following command:
```text
docker compose up
```
This spins up a few containers locally. The API will be available at http://localhost:8000.
To use in a production environment, you need to set environment variables first. Here's an
[example env file](example.env) to reference.
```text
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
