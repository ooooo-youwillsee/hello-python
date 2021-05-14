# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2

import os

# 爬取斗鱼颜值区的主播图片
class DouyuScrapyPipeline(object):
    def __init__(self):
        self.directory = "/Users/ooooo/code/PythonProjects/scrapy-learning/douyu_scrapy/images"
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def process_item(self, item, spider):
        room_id = item["room_id"]
        vertical_src = item["vertical_src"]
        headers = {
            "User-Agent":"ios/3.740 (ios 11.3; ; iPhone 6 (A1549/A1586))"
        }
        request = urllib2.Request(vertical_src,headers=headers)
        image = urllib2.urlopen(request).read()
        with open(self.directory+"/{0}.jpg".format(str(room_id)),"wb") as f:
            f.write(image)
        return item
