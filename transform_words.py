# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 09:37
# @Author  : ooooo

"""
words from spring
"""

import requests
import re
from typing import Union


class TransformWords(object):

    def __init__(self):
        self._tags = ['!DOCTYPE', 'html', 'script' 'head', 'meta', 'title', 'link', 'script', 'body', 'div',
                      'span', 'code', 'ul', 'li', 'a', 'pre', 'p', 'td', 'tr', 'table', 'i', 'h1', 'h2', 'h3', 'h4',
                      'h5', 'h6']
        self._single_patterns = [',', '\\.', '\\(', '\\)', '\\?', ';', ":", '{', "}", "<!--", "-->",
                                 '/', '[\d]+', '"', "%", "\\@", '\\[', '\\]', '!', '=', '#', '&', '\'',
                                 '\-', ' [\w] ', '<', '>', '\\+', '\\$']
        # self._tag_patterns = [re.compile('</?' + tag + r'["#=\w\s\n,:/.*-]*/?>',
        # re.IGNORECASE | re.MULTILINE) for tag in self._tags]
        self._tag_patterns = [
            re.compile(r'<script.*</script>', re.IGNORECASE | re.MULTILINE),
            re.compile(r'</?["#=\w\s\n,:/.*-]*/?>', re.IGNORECASE | re.MULTILINE),
        ]
        self._single_patterns = [re.compile(item, re.IGNORECASE | re.MULTILINE) for item in
                                 self._single_patterns]
        self._space_pattern = re.compile('[\s]{2,}|\n', re.IGNORECASE | re.MULTILINE)
        self._escape_map = {
            '&lt': '<', '&gt': '>',
        }

    def filter(self, html_str: str, replace_str='', position_str='</head>') -> list:
        if html_str.count(position_str) != 0:
            html_str = html_str[html_str.find(position_str) + len(position_str):]
        #   转义字符处理
        for k, v in self._escape_map.items():
            html_str = html_str.replace(k, v)
        html_str = self.filter_tags(html_str, replace_str)
        for _ in range(10):
            html_str = self.filter_single(html_str)
        html_str = self.filter_space_str(html_str)
        return self.split_words(html_str)

    def filter_tags(self, html_str: str, replace_str='') -> str:
        """过滤tag，返回新的字符串"""
        ans = html_str
        for pattern in self._tag_patterns:
            ans = pattern.sub(replace_str, ans)
        return ans

    def filter_single(self, html_str: str, replace_str=' ') -> str:
        """过滤单一字符，如标点符号，返回新的字符串"""
        ans = html_str
        for pattern in self._single_patterns:
            ans = pattern.sub(replace_str, ans)
        return ans

    def filter_space_str(self, html_str: str, replace_str=' ') -> str:
        """过滤空白字符"""
        return self._space_pattern.sub(replace_str, html_str)

    def split_words(self, html_str: str) -> list:
        words = html_str.split()
        print('分词前单词总数:%d' % len(words))
        ans = []
        for word in words:
            j = 0
            for i in range(len(word) + 1):
                if i == len(word) or word[i].isupper():
                    ans.append(word[j:i])
                    j = i
        ans = list(filter(lambda x: len(x) > 2, ans))
        print('分词后单词总数:%d' % len(set(ans)))
        return ans

    def request_url(self, html_url: Union[str, list], word_file_name='words.txt'):
        """请求html,过滤"""
        words = []
        if type(html_url) == str:
            html_url = [html_url]
        for url in html_url:
            words += self.filter(requests.get(url).text)
        print('总计单词:%d' % len(set(words)))
        with open(word_file_name, 'w') as f:
            f.write(' '.join(set(words)))


if __name__ == '__main__':
    spring_framework_html_url = [
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/index.html',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/overview.html#overview',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/core.html#spring-core',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/testing.html#testing',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/data-access.html#spring-data-tier',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/web.html#spring-web',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/web-reactive.html#spring-webflux',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/integration.html#spring-integration',
        'https://docs.spring.io/spring/docs/5.2.3.RELEASE/spring-framework-reference/languages.html#languages',
    ]
    transform_words = TransformWords()
    transform_words.request_url(spring_framework_html_url)
