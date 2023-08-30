from pydantic import BaseModel


class UserBaseModel(BaseModel):
    username: str


class UserModel(UserBaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserCreateModel(UserBaseModel):
    email: str
    password: str


class UserLoginModel(UserBaseModel):
    password: str
