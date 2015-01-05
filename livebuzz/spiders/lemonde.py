import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from readability.readability import Document

from livebuzz.items import LivebuzzItem

class LeMondeSpider(CrawlSpider):
    name = "lemonde"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["http://www.lemonde.fr/"]

    rules = (
        Rule(LinkExtractor(allow=('html$', )), callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            item = LivebuzzItem()
            item['title'] = response.css('h1').xpath("text()").extract()[0]
            item['url'] = response.url
            item['content'] = "pouet"
            item['keywords'] = ["pouet"]
            return item
        # response.css("a[href^='/'][href$='html']").xpath("@href").extract()
