# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PantipCrawlerItem(scrapy.Item):
    url = scrapy.Field()
    thread_id = scrapy.Field()
    title = scrapy.Field()
    topic = scrapy.Field()
    tags = scrapy.Field()
    datetime = scrapy.Field()
    comments = scrapy.Field()
