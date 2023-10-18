from sqlalchemy.ext.asyncio import AsyncSession


class CategoriesCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session
