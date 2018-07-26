#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql


def con_mysql():
    db = pymysql.connect(host='localhost', port=3306,
                         user='root', passwd='11260752', db='news', charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS poly_news")

    # 使用预处理语句创建表,标题、url、日期、摘要、图片url、内容
    sql = '''CREATE TABLE poly_news (
                 news_title  TEXT NOT NULL ,
                 news_url  TEXT ,
                 news_date TEXT ,
                 news_summary  TEXT ,
                 news_content TEXT ,
                 pic_url  TEXT
                  )DEFAULT CHARSET=utf8;'''

    cursor.execute(sql)

    print("Database is ready~")
    # 关闭数据库连接
    db.close()


def ins_mysql(title, url_n, date, content, summary, pic_url):
    # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
    db = pymysql.connect(host='localhost', port=3306, user='root', password='11260752', db='news', charset='utf8mb4',)
    # 注意数据编码为utf-8

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL两种插入格式
    sql = """
          INSERT INTO poly_news(news_title, news_url, news_date,news_summary, news_content,pic_url)
          values('%s','%s','%s','%s','%s','%s');
          """
    par = (title, url_n, date, content, summary, pic_url)
    # param = ("111", "111", "111", "111", "111", "111")

    # 执行sql语句
    cursor.execute(sql % par)  # 注意是插入一条语句
    print("OK!")
    # 提交到数据库执行
    db.commit()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

# con_mysql()
# ins_mysql('你好', '1你啊后1', '11你', '1诶集1', '1你啊后1', '11还都是')
