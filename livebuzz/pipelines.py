# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

from sqlalchemy.orm import sessionmaker
from models import Article, db_connect, create_articles_table


class ArticlePipeline(object):
    def __init__(self):
        engine = db_connect()
        create_articles_table(engine)
        self.Session = sessionmaker(bind = engine)


class ArticleValidate(ArticlePipeline):
    def process_item(self, item, spider):
        session = self.Session()

        # Check if the article has already been parsed
        if session.query(Article.id).filter(Article.url == item['url']).count() == 0:
            return item
        else:
            spider.log('Article "%s" has already been parsed' % item['title'], level=scrapy.log.DEBUG)


class ArticleSave(ArticlePipeline):
    def process_item(self, item, spider):
        if item is not None:
            session = self.Session()
            article = Article(**item)

            try:
                session.add(article)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

            return item
