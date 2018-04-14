#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编写程序读取mbox-short.txt文件，计算谁发送了最大数量的邮件。 程序查找以‘From ’开头的行，提取出改行的第二个单词即为发送 邮件的人。
# 程序创建字典，存放发送邮件的人和发送次数。创建 字典完成后，遍历字典，找出发送邮件最多的人。
name = input("Enter file:")
handle = open(name, "r")
counts = {}
for line in handle:
    if line.startswith("From "):
        words = line.split()
        wd = words[1]
        counts[wd] = counts.get(wd, 0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)