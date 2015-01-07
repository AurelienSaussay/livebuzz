# -*- coding: utf-8 -*-

from basespider import *

class LiberationSpider(BaseSpider):
    name = "liberation"
    allowed_domains = ["liberation.fr"]
    start_urls = ["http://www.liberation.fr/"]
    source = "Liberation"

    rules = (
        Rule(LinkExtractor(allow=('_[0-9]+$', ), deny=('sitemap', 'appel_temoignage', 'voiture-occasion', )), callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            return self.build_article(response)
