from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'), nullable=False)

    roadmap = relationship('Roadmap', back_populates='categories')
