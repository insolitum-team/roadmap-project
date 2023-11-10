from pydantic import BaseModel


class RoadmapBaseModel(BaseModel):
    title: str


class RoadmapModel(RoadmapBaseModel):
    id: int
    description: str
    category_id: int


class RoadmapUpdateModel(RoadmapBaseModel):
    description: str
    category_id: int


class RoadmapCreateModel(RoadmapBaseModel):
    description: str
    category_id: int
