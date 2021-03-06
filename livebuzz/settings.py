# -*- coding: utf-8 -*-

# Scrapy settings for livebuzz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'livebuzz'

SPIDER_MODULES = ['livebuzz.spiders']
NEWSPIDER_MODULE = 'livebuzz.spiders'

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'postgres',
            'password': 'pouet',
            'database': 'livebuzz'}

ITEM_PIPELINES = {
    'livebuzz.pipelines.ArticleValidate': 300,
    'livebuzz.pipelines.ArticleSave': 600,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'livebuzz (+http://www.yourdomain.com)'
