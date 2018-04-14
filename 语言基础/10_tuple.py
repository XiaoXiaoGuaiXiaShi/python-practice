#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编写程序读取mbox-short.txt文件，计算这一边每个小时发送的消息数量。程序查找以‘From ’开头的行，提取出日期中的小时。计算完成后，按小时序打印(小时，数量)对。
name = input("Enter file:")
hour = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
        words = line.split()
        wd = words[5]
        w1 = wd.split(":")
        w = w1[0]
        hour[w] = hour.get(w, 0) + 1
    else:
        continue
lst = []
for k, v in hour.items():
    newt = (v, k)
    lst.append(newt)
lst = sorted(lst, reverse=True)
print(lst)