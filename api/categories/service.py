import select
from fastapi import Depends
from api.categories.exceptions import CategoryNotFoundException

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from common.db.models.category import Category
from common.db.schemas.category import CategoryUpdateModel

from common.db.schemas.user import UserModel


class CategoryService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_category(
        self, data: CategoryUpdateModel, user: UserModel
    ) -> Category:
        category = Category(
            name=data.name,
            description=data.description,
        )
        self.session.add(category)
        await self.session.commit()
        return category

    async def get_category(self, id: int, user: UserModel) -> Category:
        stmt = select(Category).filter(Category.id == id)
        result = await self.session.execute(stmt)
        return_category = result.scalars().first()
        if not return_category:
            CategoryNotFoundException()
        return return_category

    async def get_categories(self, user: UserModel) -> list[Category]:
        stmt = select(Category)
        result = await self.session.execute(stmt)
        categories = result.scalars().all()
        if not categories:
            raise CategoryNotFoundException(
                detail="No categories found",
            )
        return categories

    async def update_category(
        self, id: int, data: CategoryUpdateModel, user: UserModel
    ) -> Category:
        stmt = select(Category).filter(Category.id == id)
        result = await self.session.execute(stmt)
        return_category = result.scalars().first()
        if not return_category:
            raise CategoryNotFoundException()
        return_category.name = data.name
        return_category.description = data.description
        await self.session.commit()
        return return_category

    async def delete_category(
        self,
        id: int,
        user: UserModel,
    ) -> Category:
        stmt = select(Category).filter(Category.id == id)
        result = await self.session.execute(stmt)
        return_category = result.scalars().first()
        if not return_category:
            raise CategoryNotFoundException()
        await self.session.delete(return_category)
        await self.session.commit()
        return return_category
