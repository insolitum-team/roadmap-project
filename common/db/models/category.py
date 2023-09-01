from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from common.db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    roadmaps = relationship("Roadmap", back_populates="category")
