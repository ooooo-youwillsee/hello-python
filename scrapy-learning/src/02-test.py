# coding=utf-8

# 百度贴吧

"""
GET /f?kw=cocos2dx&ie=utf-8&pn=50 HTTP/1.1
Host	tieba.baidu.com
User-Agent	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept	*/*
Referer	http://tieba.baidu.com/f?ie=utf-8&kw=cocos2dx&fr=search
Accept-Encoding	gzip, deflate
Accept-Language	zh-CN,zh;q=0.9,en;q=0.8
Cookie	BAIDUID=7CBB9330CE3EE5B9D72560236701DD85:FG=1; BIDUPSID=7CBB9330CE3EE5B9D72560236701DD85; PSTM=1523445739; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; TIEBA_USERTYPE=3815652c41512dabe90d7df7; bdshare_firstime=1523492636913; TIEBAUID=4f2f81482bfa5db61fa64a87; H_PS_PSSID=1435_21094_22158; BDSFRCVID=kw4sJeC629rzzsnAcf_tuG1bntEp5_JTH6ao7hX4tv7xxe9KgdxAEG0Pqx8g0KubMVkPogKKyeOTHuOP; H_BDCLCKID_SF=tJPJoKDbJKD3HnRY-PR5bJDBbeTb5RjJ-KTKQJOSHJrqfKvc5TO5y4LdjGK8bJTE-KoC3bQ7bP5nhJok5Mo2jq4p3-Aq544f2N-JLPL5MPnqbqvTbb7NQfbQ0hQOqP-jW5Ta2xQoLn7JOpvwbfnxybLg0a62btt_tJFfoU5; BDUSS=Vqa0NBQk1oc1RSfnE4TUE2emdFMmxGME9JQlA4QTZzMnlac2dIdFN4MFhyUFZhQVFBQUFBJCQAAAAAAAAAAAEAAAACO%7EE2t-e3429rAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcfzloXH85aSE; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; STOKEN=d17efc3f8a3bf722ecd307660600160463d95a29ede48c8bb7005764e704753b; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1523615611,1523798480,1523867463,1523966274; 921778946_FRSVideoUploadTip=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1523966428
Connection	keep-alive
"""

import urllib
import urllib2
import os

file_prefix = os.getcwd() + "/../data"


def loadPage(url, keyword, startPage, endPage):
    """

    :param url: 爬虫的url
    :param keyword: 关键字
    :param startPage: 开始页
    :param endPage: 终止页
    :return:
    """
    for i in range(startPage, endPage + 1):
        pn = (i - 1) * 50
        param = {
            "kw": keyword,
            "ie": "utf-8",
            "pn": str(pn)
        }
        url = url + "?" + urllib.urlencode(param)
        request = urllib2.Request(url, headers=headers)
        print("---正在连接---")
        response = urllib2.urlopen(request)
        print("---正在下载网页---")
        downPage(response.read(), "第" + str(i) + "页.html")
        print("---已经下载网页---")

    print("---完成！！！---")


def downPage(content, filename):
    """
    下载网页
    :param content: 网页内容
    :param filename: 保存的文件名
    :return:
    """
    print(file_prefix + "/" + filename)
    with open(file_prefix + "/" + filename, "w") as f:
        f.write(content)


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Cookie": "BAIDUID=7CBB9330CE3EE5B9D72560236701DD85:FG=1; BIDUPSID=7CBB9330CE3EE5B9D72560236701DD85; PSTM=1523445739; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; TIEBA_USERTYPE=3815652c41512dabe90d7df7; bdshare_firstime=1523492636913; TIEBAUID=4f2f81482bfa5db61fa64a87; H_PS_PSSID=1435_21094_22158; BDSFRCVID=kw4sJeC629rzzsnAcf_tuG1bntEp5_JTH6ao7hX4tv7xxe9KgdxAEG0Pqx8g0KubMVkPogKKyeOTHuOP; H_BDCLCKID_SF=tJPJoKDbJKD3HnRY-PR5bJDBbeTb5RjJ-KTKQJOSHJrqfKvc5TO5y4LdjGK8bJTE-KoC3bQ7bP5nhJok5Mo2jq4p3-Aq544f2N-JLPL5MPnqbqvTbb7NQfbQ0hQOqP-jW5Ta2xQoLn7JOpvwbfnxybLg0a62btt_tJFfoU5; BDUSS=Vqa0NBQk1oc1RSfnE4TUE2emdFMmxGME9JQlA4QTZzMnlac2dIdFN4MFhyUFZhQVFBQUFBJCQAAAAAAAAAAAEAAAACO%7EE2t-e3429rAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcfzloXH85aSE; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; STOKEN=d17efc3f8a3bf722ecd307660600160463d95a29ede48c8bb7005764e704753b; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1523615611,1523798480,1523867463,1523966274; 921778946_FRSVideoUploadTip=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1523966428"
}
if __name__ == '__main__':
    keyword = raw_input("输入你要查询的贴吧名：")
    startPage = int(raw_input("输入的开始页："))
    endPage = int(raw_input("输入的终止页："))
    url = "http://tieba.baidu.com/f"
    loadPage(url, keyword, startPage, endPage)
