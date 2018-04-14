#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 重写你的计算员工工作量的程序，使用try和except 来处理当用户输入非数值的问题。
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hours = int(hours)
    rate = int(rate)
    if 0 < hours < 40:
        pay = hours * rate
    elif hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = 0
    print("Pay:{}".format(pay))
except:
    print("Error, please enter numeric input")
