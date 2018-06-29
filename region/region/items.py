# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RegionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    p_code = scrapy.Field() #上级编码
    name = scrapy.Field()   #城市名称
    code = scrapy.Field()   #城市编码
    url = scrapy.Field()    #城市链接
    level = scrapy.Field()  #城市级别
    pass
