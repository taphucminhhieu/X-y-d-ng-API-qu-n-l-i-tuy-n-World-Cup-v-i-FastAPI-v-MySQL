from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WorldCup(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String(50))
    coach_name = Column(String(100))
    group_name = Column(String(100))
    point = Column(Integer)
