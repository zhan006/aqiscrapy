# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeijingaqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address=scrapy.Field()
    AQI=scrapy.Field()
    PM25=scrapy.Field()
    PM10=scrapy.Field()
    
