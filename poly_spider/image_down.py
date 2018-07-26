#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib


def ima_down(img, num):
    # 定义图片下载的路径
    path = "/Users/dqq/PycharmProjects/python-practice/poly_spider/image/"
    f = open(path + str(num) + '.jpg', 'wb')  # 注意第二个参数要写成wb，写成w会报错
    req = urllib.request.urlopen(img)
    buf = req.read()
    f.write(buf)
    f.close()