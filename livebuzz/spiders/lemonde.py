# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import lxml
import re

from w3lib.html import remove_tags

from readability.readability import Document

from livebuzz.items import ArticleItem

syntax = set(["le", "la", "les", "l'", "un", "une", "des", "d'", "du", "de", "la", "des", "de", "au", "aux", "du", "des", "ce", "cet", "cette", "ces", "mon", "ton", "son", "ma", "ta", "sa", "mes", "tes", "ses", "notre", "votre", "leur", "nos", "vos", "leurs", "quel", "quelle", "quels", "quelles", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingts", "quatre-vingt-dix", "aucun", "aucune", "aucuns", "aucunes", "maint", "mainte", "maints", "maintes", "quel", "que", "quelle", "que", "quels", "que", "quelles", "que", "tel", "telle", "tels", "telles", "tout", "toute", "tous", "toutes", "chaque", "plusieurs", "divers", "autre", "autres", "même", "mêmes", "quelque", "quelques", "quelconque", "quelconques", "certain", "certaine", "certains", "certaines", "divers", "diverse", "divers", "diverses", "différent", "différente", "différents", "différentes", "nul", "nulle", "nuls", "nulles", "leur", "leurs", "qui", "que", "quoi", "lequel", "laquelle", "lesquels", "lesquelles",
              "c", "en", "et", "est", "a", "à", "n", "qu", "l", "ou", "avec",
              "je", "tu", "il", "elle", "nous", "vous", "ils", "elles",
              "dit"])

class LeMondeSpider(CrawlSpider):
    name = "lemonde"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["http://www.lemonde.fr/"]

    rules = (
        Rule(LinkExtractor(allow=('html$', ), deny=('sitemap', 'appel_temoignage', )), callback='parse_link'),
    )

    def parse_link(self, response):
        if len(response.css('h1').xpath('text()')) > 0:
            item = ArticleItem()
            article = remove_tags(Document(response.body).summary())
            item['url'] = response.url
            item['source'] = "Le Monde"
            item['title'] = response.css('h1').xpath("text()").extract()[0].strip()
            #content = lxml.html.document_fromstring(article, parser = lxml.html.HTMLParser(encoding='utf-8')).text_content()
            words = set(re.findall(r"[\w]+", article, flags = re.UNICODE | re.IGNORECASE))
            item['keywords'] = list(words.difference(syntax))
            return item
        # response.css("a[href^='/'][href$='html']").xpath("@href").extract()
