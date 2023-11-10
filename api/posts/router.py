from fastapi import APIRouter, Depends
from api.auth.service import get_current_user
from api.posts.service import PostService
from common.db.schemas.post import PostCreateModel, PostUpdateModel

from common.db.schemas.user import UserModel

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("")
async def create_post(
    data: PostCreateModel,
    user: UserModel = Depends(get_current_user),
    service: PostService = Depends(),
):
    try:
        data = await service.create_post(data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.get("/post/{id}")
async def get_post(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: PostService = Depends(),
):
    try:
        data = await service.get_post(id=id, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.get("")
async def get_posts(
    user: UserModel = Depends(get_current_user), service: PostService = Depends()
):
    try:
        data = await service.get_posts(user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.put("/post/{id}")
async def update_post(
    id: int,
    data: PostUpdateModel,
    user: UserModel = Depends(get_current_user),
    service: PostService = Depends(),
):
    try:
        data = await service.update_step(id=id, data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.delete("/post/{id}")
async def delete_post(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: PostService = Depends(),
):
    try:
        data = await service.delete_post(id=id, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
