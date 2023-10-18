from fastapi import Depends
from common.db.crud import StepsCRUD

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class StepsService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.crud = StepsCRUD(session)
