import pytest
from httpx import AsyncClient
from sqlalchemy import select

from common.db.models import User
from tests.conftest import async_session_maker


@pytest.mark.asyncio
async def test_sign_up(ac: AsyncClient):
    response = await ac.post(
        "/auth/sign-up",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "password",
        },
    )
    assert response.status_code == 200
    async with async_session_maker() as session:
        query = select(User).filter_by(username="test")
        result = await session.execute(query)
        assert result.scalar()
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


@pytest.mark.asyncio
async def test_sign_in(ac: AsyncClient):
    response = await ac.post(
        "/auth/sign-in",
        json={
            "username": "test",
            "password": "password",
        },
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]
