from fastapi import Depends
from sqlalchemy import select
from api.roadmaps.exceptions import RoadmapNotFoundException

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.models.roadmap import Roadmap
from common.db.schemas.roadmap import RoadmapCreateModel
from common.db.schemas.user import UserModel


class RoadmapService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_roadmap(
        self, data: RoadmapCreateModel, user: UserModel
    ) -> Roadmap:
        roadmap = Roadmap(
            name=data.name,
            description=data.description,
        )
        self.session.add(roadmap)
        await self.session.commit()
        return roadmap

    async def get_roadmap(self, id: int, user: UserModel) -> Roadmap:
        stmt = select(Roadmap).filter(Roadmap.id == id)
        result = await self.session.execute(stmt)
        return_roadmap = result.scalars().first()
        if not return_roadmap:
            RoadmapNotFoundException()
        return return_roadmap

    async def get_roadmaps(self, user: UserModel) -> list[Roadmap]:
        stmt = select(Roadmap)
        result = await self.session.execute(stmt)
        roadmaps = result.scalars().all()
        if not roadmaps:
            raise RoadmapNotFoundException(
                detail="No roadmaps found",
            )
        return roadmaps

    async def update_roadmap(
        self, id: int, data: RoadmapCreateModel, user: UserModel
    ) -> Roadmap:
        stmt = select(Roadmap).filter(Roadmap.id == id)
        result = await self.session.execute(stmt)
        return_roadmap = result.scalars().first()
        if not return_roadmap:
            raise RoadmapNotFoundException()
        return_roadmap.title = data.title
        return_roadmap.description = data.description
        return_roadmap.category_id = data.category_id
        await self.session.commit()
        return return_roadmap

    async def delete_roadmap(
        self,
        id: int,
        user: UserModel,
    ) -> Roadmap:
        stmt = select(Roadmap).filter(Roadmap.id == id)
        result = await self.session.execute(stmt)
        return_roadmap = result.scalars().first()
        if not return_roadmap:
            raise RoadmapNotFoundException()
        await self.session.delete(return_roadmap)
        await self.session.commit()
        return return_roadmap
