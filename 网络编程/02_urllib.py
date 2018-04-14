#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.poly.com.cn/s/1077-3768-17655.html')
for line in fhand:
    print(line.decode().strip())