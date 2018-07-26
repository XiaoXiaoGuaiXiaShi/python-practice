#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib import request
import gzip


# 对搜狐新闻内容进行信息提取
def news_message(href_n):
    USER_AGENT = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'
    req = request.Request(href_n, headers={'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip'})
    htmlpage = request.urlopen(req).read()
    htmlpage = gzip.decompress(htmlpage).decode("UTF-8")  # 获取网页url后进行解析发现乱码，因为有些网站进行了gzip压缩

    soup_c = BeautifulSoup(htmlpage, "html5lib")

    # 获取标题
    title_f = soup_c.find_all("h1")
    title = title_f[0].text
    # print(title)

    # 获取url
    url_n = href_n
    # print(url_n)

    # 日期
    date_f = soup_c.find_all(id="news-time")
    date = date_f[0].string
    # print(date)

    # 内容
    content_f = soup_c.find_all(id="mp-editor")
    content = content_f[0].text
    # print(content)

    # 摘要
    summary = content[:100]+'......'
    # print(summary)

    # 图片url
    pic_url_s = soup_c.find_all("img")
    pic_url = []
    for i in pic_url_s:
        pic_url_a = i.get("src")
        pic_url.append(pic_url_a)
    # print(pic_url)

    print("OK I got all the news_message!")
    print(title)
    return title, url_n, date, content, summary, pic_url

# news_message("http://www.sohu.com/a/232143883_432657")