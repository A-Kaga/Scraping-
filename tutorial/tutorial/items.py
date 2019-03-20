# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class ExItem(scrapy.Item):
    name = scrapy.Field()
    posted = scrapy.Field()
    language = scrapy.Field()
    rating_counts = scrapy.Field()
    rating_average = scrapy.Field()
    favorited = scrapy.Field()
    url = scrapy.Field()
    parody = scrapy.Field()
    character = scrapy.Field()
    group = scrapy.Field()
    artist = scrapy.Field()
    female = scrapy.Field()
