from pydantic import BaseModel, ConfigDict


class UserBaseModel(BaseModel):
    username: str


class UserModel(UserBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str


class UserCreateModel(UserBaseModel):
    email: str
    password: str


class UserUpdateModel(UserBaseModel):
    email: str
    password: str


class UserLoginModel(UserBaseModel):
    password: str
