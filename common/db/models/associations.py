
from sqlalchemy import Column, ForeignKey, Integer, Table
from common.db.database import Base

user_roadmap_association = Table(
    'user_roadmap_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('roadmap_id', Integer, ForeignKey('roadmaps.id'))
)
