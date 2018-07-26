#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from baidu_news import get_soup, page_title
from soufangwang_get_message import page_content, News
from con_mysql import mysql_deal, ins_mysql
import pymysql


if __name__ == '__main__':
    keyword_name = input("Enter keyword:")   # 输入关键字
    if len(keyword_name) < 1:
        keyword_name = "保利"
    soup = get_soup(keyword_name)
    href_l = page_title(soup)
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "11260752", "news")  # 第二个参数为用户名，第三个密码，第四个是数据库名
    news = News()     # 建立新闻对象
    db = mysql_deal(db)
    for href in href_l:
        news_n = page_content(href, news)
        print(news_n.date, news_n.content)
        ins_mysql(db, news_n)
