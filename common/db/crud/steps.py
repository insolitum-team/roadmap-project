from sqlalchemy.ext.asyncio import AsyncSession


class StepsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session
