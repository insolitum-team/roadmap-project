from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Roadmap(Base):
    __tablename__ = 'roadmaps'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='roadmaps')
    steps = relationship('Step', back_populates='roadmap')
    categories = relationship('Category', back_populates='roadmap')
