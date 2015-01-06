# -*- coding: utf-8 -*-

from basespider import *

class LeMondeSpider(BaseSpider):
    name = "lemonde"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["http://www.lemonde.fr/"]
    source = "Le Monde"

    rules = (
        Rule(LinkExtractor(allow=('html$', ), deny=('sitemap', 'appel_temoignage', 'voiture-occasion', )), callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            return self.build_article(response)
