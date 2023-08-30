from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.models import User


class UserCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

    async def get_user(self, username: str) -> User:
        query = select(User).filter(User.username == username)
        result = await self.session.execute(query)
        return result.scalar()
