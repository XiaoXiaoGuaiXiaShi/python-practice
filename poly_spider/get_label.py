#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# 获取标签链接
def label_url(href):
    page_n = urllib.request.urlopen(href).read()
    soup_n = BeautifulSoup(page_n, 'html.parser')
    label = soup_n.find_all("ul", class_="accordion-3")
    href_f = label[0].contents
    href_n = []
    for i in href_f:
        if i.name == "li":
            j = i.contents[1].get("href")    # 获取a标签的href链接
            href_n.append(j)
    print("OK I got all the title_url!")
    print(href_n)
    return href_n

# href_n = label_url("http://www.poly.com.cn/1076.html")
# print(href_n)