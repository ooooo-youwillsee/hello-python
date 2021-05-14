# coding=utf-8

# 有道翻译POST请求

"""
POST /translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host	fanyi.youdao.com
Content-Length	241
Accept	application/json, text/javascript, */*; q=0.01
Origin	http://fanyi.youdao.com
X-Requested-With	XMLHttpRequest
User-Agent	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Content-Type	application/x-www-form-urlencoded; charset=UTF-8
Referer	http://fanyi.youdao.com/
Accept-Encoding	gzip, deflate
Accept-Language	zh-CN,zh;q=0.9,en;q=0.8
Cookie	OUTFOX_SEARCH_USER_ID_NCOO=1232975403.0571249; _ga=GA1.2.1199392238.1523495715; OUTFOX_SEARCH_USER_ID=-1590472375@223.11.185.8; JSESSIONID=abcBqn_e0Ct23c6AjXrlw; _ntes_nnid=851430a220a72e2a3a496551ffe21d1c,1523937744927; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1523969192975
Connection	keep-alive


i=我是中国人&from=zh-CHS&to=en&smartresult=dict&client=fanyideskweb&salt=1523969192979&sign=6303eeeb2e64240661c1a21081146bb5&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
"""

import urllib
import urllib2

# keyword = raw_input("请输入翻译的中文：")

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Origin": "http://fanyi.youdao.com",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Referer": "http://fanyi.youdao.com/",
    # "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1232975403.0571249; _ga=GA1.2.1199392238.1523495715; OUTFOX_SEARCH_USER_ID=-1590472375@223.11.185.8; JSESSIONID=abcBqn_e0Ct23c6AjXrlw; _ntes_nnid=851430a220a72e2a3a496551ffe21d1c,1523937744927; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1523969192975"

}
# data = {
#     "i": "ok",
#     "from": "AUTO",
#     "to": "AUTO",
#     # "smartresult": "dict",
#     "client": "fanyideskweb",
#     # "salt": "1523973373523",
#     # "sign": "1ac00586d4685fcab2e708899ab6b5a2",
#     "doctype": "json",
#     "version": "2.1",
#     "keyfrom": "fanyi.web",
#     "action": "FY_BY_REALTIME",
#     "typoResult": "true"
# }
# data = urllib.urlencode(data)
#     # .encode('utf-8')
# print(data)
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request, data=data)
# print(response.read())

keyword = str(raw_input("请输入翻译的中文："))

# urllib.quote 用于字符串
# urllib.urlencode 用于字典

keyword = urllib.quote(keyword)
url = "http://www.youdao.com/w/" + keyword
print(url)
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
print(response.read())