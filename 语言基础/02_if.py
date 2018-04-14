#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编写程序计算员工工作量，超过40小时的部分 Rate以1.5倍计算。
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = input("Enter Hours:")
rate = input("Enter Rate:")
hours = int(hours)
rate = int(rate)
if 0 < hours < 40:
    pay = hours * rate
elif hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = 0
print("Pay:{}".format(pay))