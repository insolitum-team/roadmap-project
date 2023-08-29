from fastapi import Depends
from common.db.crud.roadmaps import RoadmapsCRUD

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class RoadmapsService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.crud = RoadmapsCRUD(session)

    async def get_roadmaps_by_category(self, category: str):
        roadmaps = await self.crud.get_roadmaps_by_category(category=category)
        return roadmaps
