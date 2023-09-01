from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from common.db.database import Base


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    roadmap_id = Column(Integer, ForeignKey("roadmaps.id"), nullable=False)

    roadmap = relationship("Roadmap", back_populates="steps")
    posts = relationship("Post", back_populates="step")
