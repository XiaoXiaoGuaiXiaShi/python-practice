#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse, urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup
import sys
import gzip
import re
import chardet


# url = "http://news.gz.fang.com/open/28353686.html"
# htmlpage = urllib.request.urlopen(url).read()
# htmlpage=gzip.decompress(htmlpage).decode('GBK')   # 获取网页url后进行解析发现乱码，因为有些网站进行了gzip压缩
# soup_c = BeautifulSoup(htmlpage, "html5lib")
# date_c = soup_c.find_all("div", class_="comment clearfix")   # date_c的type:<class 'bs4.element.ResultSet'>
# date = date_c[0].contents[5].string
# print(date)
# # content_c = soup_c.find_all("div", class_="news-text")   # content_c的type:<class 'bs4.element.ResultSet'>



# content_str = ""
# for i in content_c:
#     # print(i.get_text())    # 获取文字内容
#     content_str = content_str + i.get_text()
# print(content_str)
# summary_1 = soup_c.find_all(attrs={"name": "description"})    # 根据tag属性提取meta元素
# print(summary_1[0]['content'])


# print(soup_c)
# 处理html页面
# date_c = soup_c.find_all("img")    # type: <class 'bs4.element.ResultSet'>
# date_f = []
# for date_o in date_c:    # type: <class 'bs4.element.Tag'>
#     if date_o.get("data-s") is None:    # 判断是否为新闻内图片
#        continue
#     else:
#         a = date_o['src']
#         if a[:4] == "http":        # 提取图片url
#             # date_f.append(a)

# data1 = urllib.request.urlopen('http://news.gz.fang.com/open/28353686.html').read()
# # 用chardet进行内容分析
# chardit1 = chardet.detect(data1)
# print(chardit1['encoding']) # baidu         print(a)


# Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
# data1 = urllib.request.urlopen(urllib.request.Request('http://news.gz.fang.com/open/28353686.html')).read()
# chardit1 = chardet.detect(data1)
# print(chardit1['encoding'])


# data1 = urllib.request.urlopen("http://news.gz.fang.com/open/28353686.html").info().getparam('charset')
# print(data1)

from con_mysql import ins_mysql
from soufangwang_get_message import News
import pymysql

news = News()
news = {
    "www.baidu.com",
    "topic",
    "2019.1.23",
    "12345677",
    "1234",
    "www.baidu.html"
}
db = pymysql.connect("localhost", "root", "11260752", "news")# 第二个参数为用户名，第三个密码，第四个是数据库名


ins_mysql(db, news)
print("OK")