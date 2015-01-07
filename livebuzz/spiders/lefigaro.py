# -*- coding: utf-8 -*-

from basespider import *

class LeFigaroSpider(BaseSpider):
    name = "lefigaro"
    allowed_domains = ["lefigaro.fr"]
    start_urls = ["http://www.lefigaro.fr/"]
    source = "Le Figaro"

    rules = (
        Rule(LinkExtractor(allow=('php$', ), deny=('sitemap', 'appel_temoignage', 'voiture-occasion', )), callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            return self.build_article(response)
