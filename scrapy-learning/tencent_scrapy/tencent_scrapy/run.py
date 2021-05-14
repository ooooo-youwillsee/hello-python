# coding=utf-8

from scrapy import cmdline

spiderName = "tencent-spider"
cmd = "scrapy crawl {0}".format(spiderName)
cmdline.execute(cmd.split())
