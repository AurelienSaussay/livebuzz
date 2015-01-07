# -*- coding: utf-8 -*-

from basespider import *

class LeParisienSpider(BaseSpider):
    name = "leparisien"
    allowed_domains = ["www.leparisien.fr"]
    start_urls = ["http://www.leparisien.fr/"]
    source = "Le Parisien"

    rules = (
        Rule(LinkExtractor(allow=('-[0-9]+\.php$'),
                           deny=('sitemap', '/accueil/', 'circulation-direct', 'code-promo')),
                           callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            return self.build_article(response)
