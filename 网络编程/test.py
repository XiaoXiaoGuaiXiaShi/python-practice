#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
page_f = urllib.request.urlopen("http://www.poly.com.cn/l/1089-3818-65.html").read()
soup_f = BeautifulSoup(page_f, 'html.parser')
link_f = soup_f.find_all("a", class_="i-pager-next")
if link_f:
        print("1")
else:
        print("OK")