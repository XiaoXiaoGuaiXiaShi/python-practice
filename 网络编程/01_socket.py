#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.poly.com.cn', 80))
cmd = 'GET http://www.poly.com.cn/s/1077-3768-17655.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    try:
        print(data.decode('utf-8', 'ignore'), end='')
    except:
        continue
mysock.close()

