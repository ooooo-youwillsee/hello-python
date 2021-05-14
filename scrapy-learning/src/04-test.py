# coding=utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib2

# 如果没有在环境变量指定PhantomJS位置
driver = webdriver.PhantomJS(executable_path="./exec/phantomjs")
i = 0
for page_num in range(1,27) :
    driver.get("http://www.quanjing.com/search.aspx?q=%E6%9E%81%E5%85%89#%E6%9E%81%E5%85%89||1|200|"+str(page_num)+"|2|||||")

    # 获取页面名为 wrapper的id标签的文本内容
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), 'lxml')

    for item in soup.find_all(id="gallery-list")[0].find_all('img'):
        image_url = item.attrs['m']
        print(image_url)
        request = urllib2.Request(image_url)
        response = urllib2.urlopen(request)
        with open("./picture/img%s.jpg" % i, "w") as f:
            f.write(response.read())
            i += 1
