# -*- coding: utf-8 -*-
import scrapy
from tencent_scrapy.items import TencentScrapyItem


#  爬取腾讯的社招职位
class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent-spider'
    allowed_domains = ['tencent.com']
    pageNum = 0
    start_urls = ['https://hr.tencent.com/position.php?&start={0}#a'.format(str(pageNum * 10))]

    def parse(self, response):
        for node in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            try:
                item = TencentScrapyItem()
                # 职位名称
                # extract() 把文本变为unicode编码
                item["positionName"] = node.xpath(".//a/text()").extract()[0].encode("utf-8")
                # 职位类别
                item["positionType"] = node.xpath('.//td[2]/text()').extract()[0].encode("utf-8")
                # 职位人数
                item["positionPeopleNum"] = node.xpath('.//td[3]/text()').extract()[0].encode("utf-8")
                # 职位地点
                item["positionAddress"] = node.xpath('.//td[4]/text()').extract()[0].encode("utf-8")
                # 职位时间
                item["positionTime"] = node.xpath('.//td[5]/text()').extract()[0].encode("utf-8")
            except:
                pass

            yield item

        if self.pageNum < 394:
            self.pageNum += 1
        url = 'https://hr.tencent.com/position.php?&start={0}#a'.format(str(self.pageNum * 10))
        yield scrapy.Request(url=url, callback=self.parse)
