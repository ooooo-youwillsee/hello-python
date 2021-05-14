# coding=utf-8


from scrapy import cmdline

spiderName = "yanzhi-spider"
cmd = "scrapy crawl "+spiderName
cmdline.execute(cmd.split())