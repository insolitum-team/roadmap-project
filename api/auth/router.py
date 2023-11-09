from fastapi import APIRouter, Depends

from api.auth.service import AuthService
from common.db.schemas import TokenModel, UserCreateModel, UserLoginModel

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/sign-up", response_model=TokenModel)
async def sign_up(data: UserCreateModel, service: AuthService = Depends()):
    return await service.register_user(data=data)


@router.post("/sign-in", response_model=TokenModel)
async def sign_in(data: UserLoginModel, service: AuthService = Depends()):
    return await service.authenticate_user(
        username_or_email=data.username, password=data.password
    )
