from fastapi import APIRouter, Depends
from api.auth.service import get_current_user
from api.steps.service import StepService
from common.db.schemas.step import StepCreateModel, StepUpdateModel

from common.db.schemas.user import UserModel

router = APIRouter(prefix="/steps", tags=["steps"])


@router.post("")
async def create_step(
    data: StepCreateModel,
    user: UserModel = Depends(get_current_user),
    service: StepService = Depends(),
):
    try:
        data = await service.create_step(data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.get("/step/{id}")
async def get_step(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: StepService = Depends(),
):
    try:
        data = await service.get_step(id=id, user=user)
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
async def get_steps(
    user: UserModel = Depends(get_current_user), service: StepService = Depends()
):
    try:
        data = await service.get_steps(user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.put("/step/{id}")
async def update_step(
    id: int,
    data: StepUpdateModel,
    user: UserModel = Depends(get_current_user),
    service: StepService = Depends(),
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


@router.delete("/step/{id}")
async def delete_step(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: StepService = Depends(),
):
    try:
        data = await service.delete_step(id=id, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
