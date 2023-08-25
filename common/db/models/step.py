from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Step(Base):
    __tablename__ = 'steps'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'), nullable=False)
    parent_step_id = Column(Integer, ForeignKey('steps.id'))

    roadmap = relationship('Roadmap', back_populates='steps')
    child_steps = relationship('Step', back_populates='parent_step', remote_side=[id])
    posts = relationship('Post', back_populates='step')
    parent_step = relationship('Step', remote_side=[id], back_populates='child_steps')
