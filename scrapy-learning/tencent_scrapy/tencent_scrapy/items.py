# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 腾讯的职位模型类
class TencentScrapyItem(scrapy.Item):
    # define the fields for your item here like:

    # 职位名称
    positionName = scrapy.Field()
    # 职位类型
    positionType = scrapy.Field()
    # 职位人数
    positionPeopleNum = scrapy.Field()
    # 职位地址
    positionAddress = scrapy.Field()
    # 职位时间
    positionTime = scrapy.Field()
