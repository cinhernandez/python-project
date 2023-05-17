
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   

    id = Column(Integer())
    name = Column(String())
    location = Column(String())
    date = Column(Date())
    