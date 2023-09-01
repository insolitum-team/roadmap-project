from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from common.db.models.associations import user_roadmap_association

from common.db.database import Base


class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, nullable=False)

    steps = relationship("Step", back_populates="roadmap")
    applicants = relationship(
        "User",
        secondary=user_roadmap_association,
        back_populates="roadmaps"
    )
    