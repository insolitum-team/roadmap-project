from fastapi import APIRouter, Depends
from api.auth.service import get_current_user

from api.users.service import UserService
from common.db.schemas.user import UserModel, UserUpdateModel


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/user/{id}")
async def get_user(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: UserService = Depends(),
):
    return await service.get_user(id=id, user=user)


@router.get("")
async def get_users(
    user: UserModel = Depends(get_current_user), service: UserService = Depends()
):
    return await service.get_users(user=user)


@router.put("/user/{id}")
async def update_user(
    id: int,
    data: UserUpdateModel,
    user: UserModel = Depends(get_current_user),
    service: UserService = Depends(),
):
    return await service.update_user(id=id, data=data, user=user)


@router.delete("/user/{id}")
async def delete_user(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: UserService = Depends(),
):
    return await service.delete_user(id=id, user=user)


@router.get("/current")
async def get_current_user(
    user: UserModel = Depends(get_current_user), service: UserService = Depends()
):
    return user
