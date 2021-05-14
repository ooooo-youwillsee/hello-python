# coding=utf-8

# 百度首页
import urllib2

if __name__ == '__main__':
    url = "http://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    print(response.read())
