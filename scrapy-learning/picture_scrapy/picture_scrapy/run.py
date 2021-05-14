# coding=utf-8


from scrapy import cmdline

spiderName = "pictureSpider"
cmd = "scrapy crawl "+spiderName
cmdline.execute(cmd.split())