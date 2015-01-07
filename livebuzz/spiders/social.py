# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from livebuzz.items import ShareItem

class SocialSpider(CrawlSpider):

    def start_requests(self):
        # Find articles for which there has been no new shares count for the past $period minutes
        pass

    def build_article(self, response):
        item = ArticleItem()
        doc = Document(response.body)
        item['url'] = response.url
        item['source'] = self.__class__.source
        item['title'] = re.sub(r'" (.*) "', ur'« \1 »', doc.short_title(), flags = re.UNICODE)
        words = set(re.findall(r"[\w]+", remove_tags(doc.summary()), flags = re.UNICODE | re.IGNORECASE))
        item['keywords'] = list(words)  #.difference(syntax))
        return item

    def parse_link(self, response):
        pass
