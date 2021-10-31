# Todos app

This is an example todos app.

## Tech stack used

| library / service                                         | description                   |
| --------------------------------------------------------- | ----------------------------- |
| [FastAPI](https://github.com/tiangolo/fastapi)            | web framework                 |
| [Nginx](https://github.com/nginx/nginx)                   | load balancer/ reverse proxy  |
| [Uvicorn](https://github.com/encode/uvicorn)              | ASGI HTTP server              |
| [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)    | mapper/ SQL toolkit (asyncio) |
| [Alembic](https://github.com/sqlalchemy/alembic)          | migrations tool               |
| [PostgreSQL](https://github.com/postgres/postgres)        | database server               |
| [Elasticsearch](https://github.com/elastic/elasticsearch) | search engine                 |
| [Celery](https://github.com/celery/celery)                | task queue/ scheduler         |
| [Pytest](https://github.com/pytest-dev/pytest)            | testing framework             |

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

### Creating a new migration

To create a new migration (autogenerated), run the following command:

```text
alembic revision --autogenerate -m "message"
```

Make sure to review the autogenerated migration before upgrading!
