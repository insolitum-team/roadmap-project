from pydantic import BaseModel


class StepBaseModel(BaseModel):
    title: str


class StepModel(StepBaseModel):
    id: int
    description: str
    roadmap_id: int


class StepUpdateModel(StepBaseModel):
    description: str
    roadmap_id: int


class StepCreateModel(StepBaseModel):
    description: str
    roadmap_id: int
