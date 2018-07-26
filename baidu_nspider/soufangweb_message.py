#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse, urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup
import sys
import gzip
import re
from urllib import request
import chardet


# 获取新闻信息，并将信息返回
def page_content(href):

    # news = News()  # 建立新闻对象

    # 获取处理后的网页
    # url = "http://news.gz.fang.com/open/28353686.html"
    # htmlpage = urllib.request.urlopen(href).read()

    # 判断网站编码方式
    # data1 = urllib.request.urlopen(urllib.request.Request(url,headers = Headers)).read()
    # # 用chardet进行内容分析
    # chardit1 = chardet.detect(data1)
    # encode_n = chardit1['encoding']
    # print(encode_n)

    # 先判断网页是否被压缩再分别进行处理
    USER_AGENT = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'
    req = request.Request(href, headers={'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip'})
    htmlpage = request.urlopen(req).read()
    htmlpage = gzip.decompress(htmlpage).decode("utf-8")  # 获取网页url后进行解析发现乱码，因为有些网站进行了gzip压缩

    soup_c = BeautifulSoup(htmlpage, "html5lib")
    # print(soup_c)

    # 获取标题、url
    url_n = href
    title = soup_c.find_all("h1")

    # 获取图片url
    pic_c = soup_c.find_all("img")  # type: <class 'bs4.element.ResultSet'>
    pic_f = []
    for pic_o in pic_c:  # type: <class 'bs4.element.Tag'>
        if pic_o.get("data-s") is None:  # 判断是否为新闻内图片
            continue
        else:
            a = pic_o['src']
            if a[:4] == "http":  # 提取图片url
                pic_f.append(a)
                # print(a)
    pic_url = pic_f

    # # 获取每条
    # summary_1 = soup_c.find_all(attrs={"name": "description"})  # 根据tag属性提取meta元素
    # # print(summary_1[0]['content'])
    # if summary_1 is not None:
    #     news.summary = summary_1[0]['content']

    # 获取内容、新闻概要
    content_c = soup_c.find_all("div", class_="news-text")  # content_c的type:<class 'bs4.element.ResultSet'>
    content_str = ""
    for con in content_c:
        # print(i.get_text())    # 获取文字内容
        content_str = content_str + con.get_text()
    content = content_str
    summary = content_str[:100]+"......"

    # 获取日期
    a1 = soup_c.find_all("h5", class_="fb-time")
    datea = a1[0]
    # datea = re.findall('^<h5 .*span>([0-9.]+)', a1[0])
    # print(datea)

    # print(title)
    # print(url_n)
    # print(datea)
    # print(content)
    # print(summary)
    # print(pic_url)
    return title, url_n, datea, content, summary, pic_url

# page_content("http://newhouse.sjz.fang.com/2018-05-20/28491945.htm")