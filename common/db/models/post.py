from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from common.db.database import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    step_id = Column(Integer, ForeignKey('steps.id'), nullable=False)

    user = relationship('User', back_populates='posts')
    step = relationship('Step', back_populates='posts')
