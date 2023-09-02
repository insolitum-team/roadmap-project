import pytest
from httpx import AsyncClient
from sqlalchemy import select

from common.db.models import User
from tests.conftest import async_session_maker


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "username, email, password",
    [
        ("username", "username@gmail.com", "password"),
        ("test", "test@gmail.com", "password"),
    ]
)
async def test_sign_up(
    ac: AsyncClient, username: str, email: str, password: str,
):
    response = await ac.post(
        "/auth/sign-up",
        json={
            "username": username,
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == 200
    async with async_session_maker() as session:
        query = select(User).filter_by(username=username)
        result = await session.execute(query)
        assert result.scalar()
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "username_or_email, password",
    [
        ("username", "password"),
        ("test@gmail.com", "password")
    ]
)
async def test_sign_in(ac: AsyncClient, username_or_email: str, password: str):
    response = await ac.post(
        "/auth/sign-in",
        json={
            "username": username_or_email,
            "password": password,
        },
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]
