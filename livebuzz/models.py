from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))

def create_articles_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Articles(DeclarativeBase):
    """Sqlalchemy articles model"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column('url', String)
    title = Column('title', String)
    keywords = Column('keywords', ARRAY(String))
