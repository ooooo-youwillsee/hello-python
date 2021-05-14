# -*- coding: utf-8 -*-
import scrapy
import json
import time
from douyu_scrapy.items import DouyuScrapyItem


class YanzhiSpiderSpider(scrapy.Spider):
    name = 'yanzhi-spider'
    allowed_domains = ['douyucdn.cn']
    pageNum = 0
    start_urls = [
        "https://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=50&client_sys=ios&offset={0}".format(str(pageNum))]

    def parse(self, response):
        jsonData = response.text
        yanzhi_list = json.loads(jsonData, encoding="utf-8")["data"]
        for yanzhi in yanzhi_list:
            item = DouyuScrapyItem()
            item["room_id"] = yanzhi["room_id"]
            item["room_name"] = yanzhi["room_name"]
            item["nickname"] = yanzhi["nickname"]
            item["vertical_src"] = yanzhi["vertical_src"]
            time.sleep(1)
            yield item
        if self.pageNum < 10000:
            self.pageNum += 50
        url = "https://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=50&client_sys=ios&offset={0}".format(
            str(self.pageNum))
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)
