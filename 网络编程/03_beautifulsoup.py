#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 标题、摘要、所有页数都要遍历（最后一页）
# 试分析(打印)http://www.poly.com.cn/领导动态下的所有新闻。使用urllib和 beatifulsoap

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# 获取新闻链接
def page_title(url_n):
    page_n = urllib.request.urlopen(url_n).read()
    soup_n = BeautifulSoup(page_n, 'html.parser')
    title = soup_n.find_all("a", class_="news-title")
    href_n = []
    for i in title:
        href_n.append(i.get("href"))
    return href_n

# 获取新闻内容
def page_content(url_c, filename):
    page_c = urllib.request.urlopen(url_c).read()
    soup_c = BeautifulSoup(page_c, 'html.parser')
    cont_c = soup_c.find_all(id='article_content')
    title_c = soup_c.find_all("h1")
    f = open(filename, 'a')
    f.write(title_c[0].text)
    f.write("\n")
    for i in cont_c:
        f.write(i.text)     # 将新闻内容写入文件
        f.close()
# page_content("http://www.poly.com.cn/s/1077-3818-16663.html")

if __name__ == '__main__':
    url_f = "http://www.poly.com.cn/1089.html"          # 要爬取的网络地址
    file_name = input("Enter file:")
    if len(file_name) < 1:
        file_name = "news.txt"
    while True:
        href_1 = page_title(url_f)
        for i in href_1:
            page_content(i, file_name)
        page_f = urllib.request.urlopen(url_f).read()
        soup_f = BeautifulSoup(page_f, 'html.parser')
        link_f = soup_f.find_all("a", class_="i-pager-next")
        if link_f:
            url_f = link_f[0].get("href")
            continue
        else:
            print("OK")
            break


# print(soup.prettify())    # 按照标准的缩进格式的结构输出

