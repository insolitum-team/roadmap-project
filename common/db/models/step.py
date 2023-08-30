from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from common.db.database import Base


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    roadmap_id = Column(Integer, ForeignKey("roadmaps.id"), nullable=False)
    parent_step_id = Column(Integer, ForeignKey("steps.id"))

    roadmap = relationship("Roadmap", back_populates="steps")
    posts = relationship("Post", back_populates="step")
    child_steps = relationship(
        "Step", backref="parent_step", remote_side=[id], foreign_keys=[parent_step_id]
    )
