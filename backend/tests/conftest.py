from pytest import fixture
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from backend import app
from backend.database import get_session


@fixture(scope="function")
async def session()-> AsyncSession:
    async with get_session() as session:
        yield session


@fixture(scope="module")
async def client() -> AsyncClient:
    async with AsyncClient(app=app) as client:
        yield client