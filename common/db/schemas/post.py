from pydantic import BaseModel


class PostBaseModel(BaseModel):
    title: str


class PostModel(PostBaseModel):
    id: int
    content: str
    links: list[str]
    step_id: int


class PostUpdateModel(PostBaseModel):
    content: str
    links: list[str]
    step_id: int


class PostCreateModel(PostBaseModel):
    content: str
    links: list[str]
    step_id: int
