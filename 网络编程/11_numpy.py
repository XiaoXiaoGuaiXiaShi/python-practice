#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# names = np.array(['Bob','Joe','Will','Bob','Joe'])
# data = np.random.randn(5,4)    #生成正态分布的随机数据
# print(data[names == 'Bob'])

# 对数组求更号
# arr = np.arange(10)
# print(np.sqrt(arr))

# 横向扩展、纵向扩展，可以理解为横切面
x = np.array([1,2,3])
y = np.array([4,5,6,7])
xs,ys = np.meshgrid(x,y)
print(xs)
print('#################')
print(ys)


points = np.arange(-5,5)