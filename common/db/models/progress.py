from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'), nullable=False)
    current_step_id = Column(Integer, ForeignKey('steps.id'))

    user = relationship('User', back_populates='progresses')
    roadmap = relationship('Roadmap')
    current_step = relationship('Step')
