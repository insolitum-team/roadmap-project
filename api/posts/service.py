from fastapi import Depends
from sqlalchemy import select
from api.posts.exceptions import PostNotFoundException

from common.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from common.db.models.post import Post
from common.db.schemas.post import PostCreateModel, PostUpdateModel

from common.db.schemas.user import UserModel


class PostService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_post(self, data: PostCreateModel, user: UserModel) -> Post:
        roadmap = Post(
            title=data.title,
            content=data.content,
            links=data.links,
            step_id=data.step_id,
        )
        self.session.add(roadmap)
        await self.session.commit()
        return roadmap

    async def get_post(self, id: int, user: UserModel) -> Post:
        stmt = select(Post).filter(Post.id == id)
        result = await self.session.execute(stmt)
        return_post = result.scalars().first()
        if not return_post:
            PostNotFoundException()
        return return_post

    async def get_posts(self, user: UserModel) -> list[Post]:
        stmt = select(Post)
        result = await self.session.execute(stmt)
        posts = result.scalars().all()
        if not posts:
            raise PostNotFoundException(
                detail="No posts found",
            )
        return posts

    async def update_post(
        self, id: int, data: PostUpdateModel, user: UserModel
    ) -> Post:
        stmt = select(Post).filter(Post.id == id)
        result = await self.session.execute(stmt)
        return_post = result.scalars().first()
        if not return_post:
            raise PostNotFoundException()
        return_post.title = data.title
        return_post.content = data.content
        return_post.links = data.links
        return_post.step_id = data.step_id
        await self.session.commit()
        return return_post

    async def delete_post(self, id: int, user: UserModel) -> Post:
        stmt = select(Post).filter(Post.id == id)
        result = await self.session.execute(stmt)
        return_post = result.scalars().first()
        if not return_post:
            raise PostNotFoundException()
        await self.session.delete(return_post)
        await self.session.commit()
        return return_post
