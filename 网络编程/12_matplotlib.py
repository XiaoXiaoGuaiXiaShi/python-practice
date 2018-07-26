#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame1 = pd.DataFrame(data)
print(frame1)

frame2=pd.DataFrame(data, columns=['year', 'state', 'pop'], index=['one','two','three','four','five'])
print(frame2)

frame4 = frame2.reindex(columns = ['year','pop','state'])
print(frame4)

frame5 = frame4.reindex(index = ['one','two','three','four','five'],columns = ['year','pop','state'])
print(frame5)

# 丢弃指定轴上的项 
print(frame5.drop(['four','five'],axis=0)) # axis=0表示行，axis=1表示列
