# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import re

from w3lib.html import remove_tags

from readability.readability import Document

from livebuzz.items import ArticleItem

syntax = set(["le", "la", "les", "l'", "un", "une", "des", "d'", "du", "de", "la", "des", "de", "au", "aux", "du", "des", "ce", "cet", "cette", "ces", "mon", "ton", "son", "ma", "ta", "sa", "mes", "tes", "ses", "notre", "votre", "leur", "nos", "vos", "leurs", "quel", "quelle", "quels", "quelles", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingts", "quatre-vingt-dix", "aucun", "aucune", "aucuns", "aucunes", "maint", "mainte", "maints", "maintes", "quel", "que", "quelle", "que", "quels", "que", "quelles", "que", "tel", "telle", "tels", "telles", "tout", "toute", "tous", "toutes", "chaque", "plusieurs", "divers", "autre", "autres", "même", "mêmes", "quelque", "quelques", "quelconque", "quelconques", "certain", "certaine", "certains", "certaines", "divers", "diverse", "divers", "diverses", "différent", "différente", "différents", "différentes", "nul", "nulle", "nuls", "nulles", "leur", "leurs", "qui", "que", "quoi", "lequel", "laquelle", "lesquels", "lesquelles",
              "c", "en", "et", "est", "a", "à", "n", "qu", "l", "ou", "avec",
              "je", "tu", "il", "elle", "nous", "vous", "ils", "elles",
              "dit"])

class BaseSpider(CrawlSpider):
    def build_article(self, response):
        item = ArticleItem()
        doc = Document(response.body)
        item['url'] = response.url
        item['source'] = self.__class__.source
        item['title'] = re.sub(r'" (.*) "', ur'« \1 »', doc.short_title(), flags = re.UNICODE)
        words = set(re.findall(r"[\w]+", remove_tags(doc.summary()), flags = re.UNICODE | re.IGNORECASE))
        item['keywords'] = list(words.difference(syntax))
        return item


    def parse_link(self, response):
        pass
