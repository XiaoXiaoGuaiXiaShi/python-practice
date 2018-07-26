#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "11260752", "test")  # 第二个参数为用户名，第三个密码，第四个是数据库名

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;

create table Artist(
id int NOT NULL primary key IDENTITY(1,1),
name_artist varchar(128) UNIQUE
)default charset=utf8;

create table Album(
id int NOT NULL primary key IDENTITY(1,1),
name_artist varchar(128) UNIQUE
)default charset=utf8;

create table Track(
id int NOT NULL primary key IDENTITY(1,1),
title_track varchar(128) UNIQUE,
albun_id INT ,
len int ,ra int , COUNT INT
)default charset=utf8;

''')