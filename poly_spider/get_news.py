#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# 获取当前页新闻链接
def page_url(url_n):
    page_n = urllib.request.urlopen(url_n).read()
    soup_n = BeautifulSoup(page_n, 'html.parser')
    title = soup_n.find_all("a", class_="news-title")
    href_n = []
    for i in title:
        href_n.append(i.get("href"))
    return href_n

# 获取每一页的新闻链接
def news_url(href):
    href_n = href
    href_1 = page_url(href_n)
    # print(href_1)
    news_u = href_1
    while True:
        page_f = urllib.request.urlopen(href_n).read()
        soup_f = BeautifulSoup(page_f, 'html.parser')
        link_f = soup_f.find_all("a", class_="i-pager-next")
        if link_f:
            url_f = link_f[0].get("href")    # 获取下一页网址
            # print(page_url(url_f))
            news_u.append(page_url(url_f))
            href_n = url_f     # 修改当前页网址
            continue
        else:
            print("OK I got all the news_url!")
            # print(news_u)
            return news_u
            break

news_1 = news_url('http://www.poly.com.cn/1091.html')
for i in news_1:
    # print(type(i).string)
    if type(i) == "<class 'str'>":
        print(i)
    elif type(i) == "<class 'list'>":
        for h in i:
            print(h)
    else:
        print("wrong")