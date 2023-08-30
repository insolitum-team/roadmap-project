from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from common.db.database import Base


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    roadmap_id = Column(Integer, ForeignKey("roadmaps.id"), nullable=False)
    current_step_id = Column(Integer, ForeignKey("steps.id"))

    user = relationship("User", back_populates="progresses")
    roadmap = relationship("Roadmap")
    current_step = relationship("Step")
