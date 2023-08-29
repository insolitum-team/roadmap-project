from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.models.roadmap import Roadmap


class RoadmapsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_roadmaps_by_category(self, category: str):
        query = select(Roadmap).where(Roadmap.category == category)
        result = await self.session.execute(query)
        return result.scalar()
