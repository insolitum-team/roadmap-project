from fastapi import APIRouter, Depends
from api.auth.service import get_current_user
from api.categories.service import CategoryService
from common.db.schemas.category import CategoryCreateModel, CategoryUpdateModel

from common.db.schemas.user import UserModel

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("")
async def create_category(
    data: CategoryCreateModel,
    user: UserModel = Depends(get_current_user),
    service: CategoryService = Depends(),
):
    try:
        data = await service.create_category(data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.get("/category/{id}")
async def get_category(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: CategoryService = Depends(),
):
    try:
        data = await service.get_category(id=id, user=user)
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
async def get_categories(
    user: UserModel = Depends(get_current_user), service: CategoryService = Depends()
):
    try:
        data = await service.get_categories(user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.put("/category/{id}")
async def update_category(
    id: int,
    data: CategoryUpdateModel,
    user: UserModel = Depends(get_current_user),
    service: CategoryService = Depends(),
):
    try:
        data = await service.update_category(id=id, data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.delete("/category/{id}")
async def delete_category(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: CategoryService = Depends(),
):
    try:
        data = await service.delete_category(id=id, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
