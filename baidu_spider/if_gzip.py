#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
#
# USER_AGENT = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'
#
# req = request.Request(r'http://www.qiushibaike.com/', headers={'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip'})
# res = request.urlopen(req)
#
# print(res.info().get('Content-Encoding'))

import requests
from bs4 import BeautifulSoup
import gzip
url = "http://news.gz.fang.com/open/28353396.html"
# htmlpage = urllib.request.urlopen(href).read()

# 先判断网页是否被压缩再分别进行处理

USER_AGENT = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'

req = request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip'})
htmlpage = request.urlopen(req).read()

htmlpage = gzip.decompress(htmlpage).decode('GBK')  # 获取网页url后进行解析发现乱码，因为有些网站进行了gzip压缩
soup_c = BeautifulSoup(htmlpage, "html5lib")
print(soup_c)
