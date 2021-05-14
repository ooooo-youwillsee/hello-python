# coding=utf-8

from scrapy import cmdline


if __name__ == '__main__':
    spiderName = "test-spider"
    cmd = "scrapy crawl " + spiderName
    cmdline.execute(cmd.split())
