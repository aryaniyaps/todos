from fastapi import FastAPI
from httpx import AsyncClient
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from backend import app
from backend.database import get_session


@pytest.fixture(scope="function")
async def session() -> AsyncSession:
    async with get_session() as session:
        yield session


@pytest.fixture(scope="module")
async def client() -> AsyncClient:
    async with AsyncClient(app=app) as client:
        yield client