from fastapi import Depends
from fastapi.exceptions import ValidationException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.auth.service import get_current_user
from api.users.exceptions import UserNotFoundException
from common.db.database import get_async_session

from common.db.models.user import User
from common.db.schemas.user import UserModel, UserUpdateModel


class UserService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_user(self, id: int, user: UserModel) -> User:
        stmt = select(User).filter(User.id == id)
        result = await self.session.execute(stmt)
        return_user = result.scalars().first()
        if not return_user:
            UserNotFoundException()
        return return_user

    async def get_users(self, user: UserModel) -> list[User]:
        stmt = select(User)
        result = await self.session.execute(stmt)
        users = result.scalars().all()
        if not users:
            raise UserNotFoundException(
                detail="No users found",
            )
        return users

    async def update_user(
        self, id: int, data: UserUpdateModel, user: UserModel
    ) -> User:
        stmt = select(User).filter(User.id == id)
        result = await self.session.execute(stmt)
        return_user = result.scalars().first()
        if not return_user:
            raise UserNotFoundException()
        return_user.username = data.username
        return_user.email = data.email
        return_user.password = data.password
        await self.session.commit()
        return return_user

    async def delete_user(
        self,
        id: int,
        user: UserModel,
    ) -> User:
        stmt = select(User).filter(User.id == id)
        result = await self.session.execute(stmt)
        return_user = result.scalars().first()
        if not return_user:
            raise UserNotFoundException()
        await self.session.delete(return_user)
        await self.session.commit()
        return return_user
