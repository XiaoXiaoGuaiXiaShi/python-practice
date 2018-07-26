#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
from urllib.parse import quote

# 获取BeautifulSoup解析HTML后的soup
def get_soup(keyword):
    question_word = keyword  # 输入要查找的关键字
    question_word = quote(question_word, 'utf-8')  # 对关键字进行url编码
    # 对百度新闻查取关键字url进行分析并确定最新的30条新闻的url格式
    url = "http://news.baidu.com/ns?cl=2&rn=30&tn=news&clk=sortbytime&word=" + question_word
    opener = urllib.request.build_opener()                 # 添加 user-agent进行网络请求
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')]
    htmlpage = opener.open(url).read()
    soup = BeautifulSoup(htmlpage, "html5lib")  # 注意解析器的选择
    # print(soup.prettify())
    return soup

def get_url(soup):
    c_title = soup.find_all("h3", class_="c-title")  # 根据css属性获取查找链接的父节点

    # 获取每条新闻链接
    href_n = []
    for i in c_title:
        title = i.a['href']  # 根据tag结构查找a链接的href
        href_n.append(title)  # 添加到列表
    # print(type(href_n))
    # print(href_n)
    return href_n