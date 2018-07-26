#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mysql_deal(db):     # 创建表

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS baidu_news")

    # 使用预处理语句创建表,标题、url、日期、摘要、图片url、内容
    sql = """CREATE TABLE baidu_news (
         news_title  CHAR(100) NOT NULL,
         news_url  CHAR(100),
         news_date CHAR(50),
         news_summary  TEXT,
         news_content TEXT,
         pic_url  CHAR(100)
          )"""

    cursor.execute(sql)

    print("Database is ready~")
    # 关闭数据库连接
    db.close()
    return db


# 将新闻信息存入mysql数据库中
def ins_mysql(db, news):

    cursor = db.cursor()    # 使用 cursor() 方法创建一个游标对象 cursor

    news_title = '1111'
    news_url = '111'
    news_date = '111'
    news_summary = '111'
    news_content = '111'
    pic_url = '111'

    # SQL 插入语句
    sql = '''
        insert into baidu_news (news_title, news_url, news_date, news_summary, news_content, pic_url) values (%s, %s, %s, %s, %s, %s)
    '''

    cursor.executemany(sql, [
        news_title, news_url, news_date,
        news_summary, news_content,
        pic_url
    ])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("insert success~")
        # 关闭数据库连接
        db.close()
    except:
        # 如果发生错误则回滚
        db.rollback()
        # 关闭数据库连接
        db.close()

