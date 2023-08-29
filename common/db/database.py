from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from common.settings.config import POSTGRES_NAME, POSTGRES_PORT, POSTGRES_HOST, POSTGRES_PASSWORD, POSTGRES_USER

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
Base = declarative_base()

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Function used to get object of an asynchronous session for database manipulations.

    Returns:
        Asynchronous session object

    """
    async with async_session_maker() as session:
        yield session
