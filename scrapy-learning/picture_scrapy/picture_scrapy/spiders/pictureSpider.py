# -*- coding: utf-8 -*-
import scrapy


class PicturespiderSpider(scrapy.Spider):
    name = 'pictureSpider'
    allowed_domains = ['quanjing.com']
    start_urls = ['http://www.quanjing.com/search.aspx?q=%E6%9E%81%E5%85%89#%E6%9E%81%E5%85%89||1|100|1|2|||||']

    def parse(self, response):
        with open("picture.html","w") as f:
            f.write(response.text.encode("utf-8"))
        # for item in response.xpath("//ul[@id='gallery-list']"):
        #     img_url  = item.xpath("./li").extract().encode("utf-8")
        #     print(img_url)

