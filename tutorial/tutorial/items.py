# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class ExItem(scrapy.Item):
    parody = scrapy.Field()
    character = scrapy.Field()
    group = scrapy.Field()
    artist = scrapy.Field()
