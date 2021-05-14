# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuScrapyItem(scrapy.Item):
    # "room_id": 1047629,
    # "room_name": "练琴不露脸 记得点关注",
    # "nickname": "Piano小詩",
    # "cate_id": 201,
    # "room_src": "https://rpic.douyucdn.cn/live-cover/appCovers/2018/04/09/1047629_20180409032314_small.jpg",
    # "is_vertical": 1,
    # "vertical_src": "https://rpic.douyucdn.cn/live-cover/appCovers/2018/04/09/1047629_20180409032314_big.jpg",
    room_id = scrapy.Field()
    room_name = scrapy.Field()
    nickname = scrapy.Field()
    vertical_src = scrapy.Field()
