#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from get_label import label_url
from get_news import news_url
from get_message import news_message
from con_mysql import ins_mysql
from image_down import ima_down


if __name__ == '__main__':

    # 网站“新闻动态”的链接
    url_poly = 'http://www.poly.com.cn/1076.html'

    # 获取网站所有标签链接
    label_url_list = label_url(url_poly)

    # 对每个标签链接做相同处理
    for label_u in label_url_list:
        # 获取标签链接下的所有新闻链接
        news_u = news_url(label_u)
        for i in news_u:
            if type(i) == 'str':
                # 获取每条新闻的数据
                title, url_n, date, content, summary, pic_url = news_message(i)
                # print(title)
                # print(type(url_n))
                # print(type(date))
                # print(type(content))
                # print(type(summary))
                # print(type(pic_url))    #注意pic_url的类型，不是一条插入语句了

                p_url = "".join(list(pic_url))
                # 将数据插入到数据库中
                ins_mysql(title, url_n, date, content, summary, p_url)
                # 下载每条新闻的图片
                ord = 0
                for j in pic_url:
                    ima_down(j, title+str(ord))
                    ord += 1
            elif type(i) == 'list':
                for h in i:
                    # 获取每条新闻的数据
                    title, url_n, date, content, summary, pic_url = news_message(h)
                    p_url = "".join(list(pic_url))
                    # 将数据插入到数据库中
                    ins_mysql(title, url_n, date, content, summary, p_url)
                    # 下载每条新闻的图片
                    ord = 0
                    for j in pic_url:
                        ima_down(j, title + str(ord))
                        ord += 1




