#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 读取文件regex_sum.txt，使用re.findall()查找所有整数，使用正 则表达式‘[0-9]+’，然后把摘取的字符串转换为整数，再相加，输出和。
import re
name = input("Enter the file name:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
sum1 = 0
for line in handle:
    number = re.findall('[0-9]+', line)
    for i in number:
        i = int(i)
        sum1 += i
print("sum:{}".format(sum1))
