from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

import settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))

def create_articles_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Article(DeclarativeBase):
    """Sqlalchemy articles model"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    source = Column(String)
    keywords = Column(ARRAY(String))
    shares = relationship("Share", backref="article")


class Share(DeclarativeBase):
    """Sqlalchemy shares model"""
    __tablename__ = "shares"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    count = Column(Integer)
