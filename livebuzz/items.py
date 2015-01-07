# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    keywords = scrapy.Field()

class ShareItem(scrapy.Item):
    article_id = scrapy.Field()
    count = scrapy.Field()
    time = scrapy.Field()
