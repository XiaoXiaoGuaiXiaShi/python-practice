#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打开mbox-short.txt文件，一行一行地读取，如果找到以‘From ’开头的 行，如:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 对于每一行使用split()方法进行分割，打印出该行的第二个单词(即整个邮件地址)，
# 还要打印出符合条件的行的总数。注意:不是以“From:”开头。

fname = input("Enter the file name:")
handle = open(fname, "r")
count = 0
for line in handle:
    if line.startswith("From "):
        words = line.split()
        count += 1
        print(words[1])
    else:
        continue
print("There were", count, "lines in the file with From as the first word")