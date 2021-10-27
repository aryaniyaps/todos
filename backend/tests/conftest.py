import pytest
from fastapi.testclient import TestClient

from backend import app
from backend.database import get_session


@pytest.fixture(scope="function")
async def session():
    async with get_session() as session:
        yield session

@pytest.fixture(scope="module")
def client():
    with TestClient(app=app) as client:
        yield client