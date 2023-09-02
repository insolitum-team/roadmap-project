from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.models import User


class UserCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

    async def get_user(self, username_or_email: str) -> User:
        query = select(User).filter(
            or_(User.username == username_or_email, User.email == username_or_email))
        result = await self.session.execute(query)
        return result.scalar()
