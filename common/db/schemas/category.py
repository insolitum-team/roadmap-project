from pydantic import BaseModel


class CategoryBaseModel(BaseModel):
    name: str


class CategoryModel(CategoryBaseModel):
    id: int
    description: str


class CategoryUpdateModel(CategoryBaseModel):
    description: str


class CategoryCreateModel(CategoryBaseModel):
    description: str
