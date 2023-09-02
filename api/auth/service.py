from datetime import datetime, timedelta

import jwt
from argon2 import PasswordHasher
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.exceptions import AuthenticateExecption, ValidationException
from common.db.crud import UserCRUD
from common.db.database import get_async_session
from common.db.models import User
from common.db.schemas import TokenModel, UserCreateModel, UserModel
from common.settings import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        hasher = PasswordHasher()
        return hasher.verify(hashed_password, plain_password)

    @classmethod
    def hash_password(cls, password) -> str:
        hasher = PasswordHasher()
        return hasher.hash(password)

    @classmethod
    def create_token(cls, user: User) -> TokenModel:
        data = UserModel.model_validate(user)
        payload = {
            "iat": datetime.utcnow(),
            "nbf": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(seconds=config.JWT_ACCESS_TTL),
            "sub": str(data.id),
            "user": data.model_dump(),
        }
        token = jwt.encode(
            payload=payload, key=config.JWT_SECRET, algorithm=config.JWT_ALGORITHM
        )

        return TokenModel(access_token=token)

    @classmethod
    def validate_token(cls, token: str) -> User:
        try:
            payload = jwt.decode(
                token,
                config.JWT_SECRET,
                algorithms=[config.JWT_ALGORITHM]
            )
        except jwt.PyJWTError:
            raise ValidationException()

        data = payload.get("user")

        try:
            user = User.parse_obj(data)
        except ValidationError:
            raise ValidationException()

        return user

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session
        self.crud = UserCRUD(session=session)

    async def register_user(self, data: UserCreateModel) -> TokenModel:
        user = User(
            username=data.username,
            email=data.email,
            password=self.hash_password(data.password),
        )
        await self.crud.create_user(user=user)

        return self.create_token(user)

    async def authenticate_user(self, username_or_email: str, password: str) -> TokenModel:
        user = await self.crud.get_user(username_or_email=username_or_email)

        if not user:
            raise AuthenticateExecption()

        if not self.verify_password(plain_password=password, hashed_password=user.password):
            raise AuthenticateExecption()

        return self.create_token(user)
