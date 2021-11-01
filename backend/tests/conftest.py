from fastapi import FastAPI
from httpx import AsyncClient
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_session


@pytest.fixture(scope="function")
async def session() -> AsyncSession:
    async with get_session() as session:
        yield session


@pytest.fixture(scope="module")
async def client(app) -> AsyncClient:
    async with AsyncClient(app=app) as client:
        yield client


@pytest.fixture(scope="session")
async def app() -> FastAPI:
    from backend import app
    return app