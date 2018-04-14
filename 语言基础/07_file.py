#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1、打开romeo.txt文件，一行一行地读取，对于每一行使用 split()方法进行分割。程序生成单词列表。检查每一个单词
# 是否已经在列表中，如果不在就添加，当程序结束时，对单词按
# 字母顺序进行排序并打印。

fname = input("Enter file name: ")
fh = open(fname, 'r')
wd = list()
for line in fh:
    word = line.split()
    for w in word:
        if w not in wd:
            wd.append(w)
wd = wd.sort()
print(wd)
