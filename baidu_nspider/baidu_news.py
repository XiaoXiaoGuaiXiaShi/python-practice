#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from total_news import get_soup
from total_news import get_url
from soufangweb_message import page_content
from con_mysql import ins_mysql
from image_down import ima_down
import re
from souhu_message import news_message

if __name__ == '__main__':

    # 根据关键字获取BeautifulSoup解析HTML后的新闻总网页soup
    keyword_name = input("Enter keyword:")  # 输入关键字
    if len(keyword_name) < 1:
        keyword_name = "保利"
    soup = get_soup(keyword_name)

    # 获取网页链接
    href = get_url(soup)
    print(href)

    # 对网站来源不同的网页分别进行处理
    for i in href:
        if re.search('news.tj.fang.com/', i):
            print("hello,搜房网！")
            # 获取网页信息
            title, url_n, dateaa, content, summary, pic_url = page_content(i)
            # 插入数据库
            p_url = "".join(list(pic_url))
            # 将数据插入到数据库中
            ins_mysql(title, url_n, dateaa, content, summary, p_url)
            # 下载每条新闻的图片
            ord = 0
            for j in pic_url:
                ima_down(j, title + str(ord))
                ord += 1
        elif re.search('sohu.com', i):
            print("hello,搜狐网！")
            # 获取网页信息
            title, url_n, dateaa, content, summary, pic_url = news_message(i)
            # 插入数据库
            p_url = "".join(list(pic_url))
            # 将数据插入到数据库中
            ins_mysql(title, url_n, dateaa, content, summary, p_url)
            # 下载每条新闻的图片
            ord = 0
            for j in pic_url:
                ima_down(j, title + str(ord))
                ord += 1
