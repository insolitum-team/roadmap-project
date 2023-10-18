from sqlalchemy.ext.asyncio import AsyncSession


class PostsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session
