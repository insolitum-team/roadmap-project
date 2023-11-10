from fastapi import Depends
from sqlalchemy import select
from api.steps.exceptions import StepNotFoundException

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from common.db.models.step import Step
from common.db.schemas.step import StepCreateModel, StepUpdateModel

from common.db.schemas.user import UserModel


class StepService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_step(self, data: StepCreateModel, user: UserModel) -> Step:
        roadmap = Step(
            title=data.title,
            description=data.description,
            roadmap_id=data.roadmap_id,
        )
        self.session.add(roadmap)
        await self.session.commit()
        return roadmap

    async def get_step(self, id: int, user: UserModel) -> Step:
        stmt = select(Step).filter(Step.id == id)
        result = await self.session.execute(stmt)
        return_step = result.scalars().first()
        if not return_step:
            StepNotFoundException()
        return return_step

    async def get_steps(self, user: UserModel) -> list[Step]:
        stmt = select(Step)
        result = await self.session.execute(stmt)
        steps = result.scalars().all()
        if not steps:
            raise StepNotFoundException(
                detail="No steps found",
            )
        return steps

    async def update_step(
        self, id: int, data: StepUpdateModel, user: UserModel
    ) -> Step:
        stmt = select(Step).filter(Step.id == id)
        result = await self.session.execute(stmt)
        return_step = result.scalars().first()
        if not return_step:
            raise StepNotFoundException()
        return_step.title = data.title
        return_step.description = data.description
        return_step.roadmap_id = data.roadmap_id
        await self.session.commit()
        return return_step

    async def delete_step(self, id: int, user: UserModel) -> Step:
        stmt = select(Step).filter(Step.id == id)
        result = await self.session.execute(stmt)
        return_step = result.scalars().first()
        if not return_step:
            raise StepNotFoundException()
        self.session.delete(return_step)
        await self.session.commit()
        return return_step
