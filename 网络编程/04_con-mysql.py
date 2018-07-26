#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "11260752", "test")  # 第二个参数为用户名，第三个密码，第四个是数据库名

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()