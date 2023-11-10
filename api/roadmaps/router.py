from fastapi import APIRouter, Depends
from api.auth.service import get_current_user

from api.roadmaps.service import RoadmapService
from common.db.schemas.roadmap import RoadmapCreateModel, RoadmapUpdateModel
from common.db.schemas.user import UserModel

router = APIRouter(prefix="/roadmaps", tags=["roadmaps"])


@router.post("")
async def create_category(
    data: RoadmapCreateModel,
    user: UserModel = Depends(get_current_user),
    service: RoadmapService = Depends(),
):
    try:
        data = await service.create_roadmap(data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.get("/roadmap/{id}")
async def get_roadmap(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: RoadmapService = Depends(),
):
    try:
        data = await service.get_roadmap(id=id, user=user)
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
async def get_roadmaps(
    user: UserModel = Depends(get_current_user), service: RoadmapService = Depends()
):
    try:
        data = await service.get_roadmaps(user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.put("/roadmap/{id}")
async def update_roadmap(
    id: int,
    data: RoadmapUpdateModel,
    user: UserModel = Depends(get_current_user),
    service: RoadmapService = Depends(),
):
    try:
        data = await service.update_roadmap(id=id, data=data, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@router.delete("/roadmap/{id}")
async def delete_roadmap(
    id: int,
    user: UserModel = Depends(get_current_user),
    service: RoadmapService = Depends(),
):
    try:
        data = await service.delete_roadmap(id=id, user=user)
        return {
            "status": "success",
            "data": data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
