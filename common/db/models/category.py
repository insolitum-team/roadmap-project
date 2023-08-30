from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from common.db.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'), nullable=False)

    roadmap = relationship('Roadmap', back_populates='categories')
