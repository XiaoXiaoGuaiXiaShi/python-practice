#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# 对新闻内容进行信息提取
def news_message(href_n):
    page = urllib.request.urlopen(href_n).read()
    soup = BeautifulSoup(page, 'html.parser')
    # 获取标题
    title_f = soup.find_all(id="Title")
    title = title_f[0].text
    # print(title)
    # 获取url
    url_n = href_n
    # print(url_n)
    # 日期
    date_f = soup.find_all(id="PublishTime")
    date = date_f[0].text
    # print(date)
    # 内容
    content_f = soup.find_all("p", class_="indent")
    content = content_f[0].text
    # print(content)
    # 摘要
    summary = content[:100]+'......'
    # print(summary)
    # 图片url
    pic_url_s = soup.find_all("img")
    pic_url = []
    for i in pic_url_s:
        pic_url_a = 'http://www.poly.com.cn/' + i.get("src")
        pic_url.append(pic_url_a)
    # print(pic_url)
    print("OK I got all the news_message!")
    print(title)
    return title, url_n, date, content, summary, pic_url



# get_message('http://www.poly.com.cn/s/1077-3817-17833.html')