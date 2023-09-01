from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from common.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    links = Column(JSON, default=[])
    step_id = Column(Integer, ForeignKey("steps.id"), nullable=False)

    step = relationship("Step", back_populates="posts")
