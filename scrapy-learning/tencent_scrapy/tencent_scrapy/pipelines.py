# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class TencentScrapyPipeline(object):

    def __init__(self):
        self.file = open("/Users/ooooo/code/PythonProjects/scrapy-learning/tencent_scrapy/tencent_scrapy/tencent_position.json", "w")

    # item 为类字典对象
    def process_item(self, item, spider):
        jsonData = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(jsonData+"\n")
        return item

    # spider 打开，只执行一次
    def open_spider(self, spider):
        pass

    # spider 关闭，只执行一次
    def close_spider(self, spider):
        self.file.close()
