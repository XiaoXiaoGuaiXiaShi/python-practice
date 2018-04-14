#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# str='X-OSPAM-Confidence: 0.8475 ' 写程序使用find()函数和字符串分片技术提取出冒号后面的字符串，然后将
# 它转换成浮点型数值。
str = "X-OSPAM-Confidence: 0.8475 "
place1 = str.find(":")
number = str[place1+1:]
number = number.strip()
# print(number)
number = float(number)
print(number)
