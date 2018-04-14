#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 写一个程序提示用户输入hours和每小时的rate， 然后计算净支付。
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
hours = input("Enter Hours:")
rate = input("Enter Rate:")
pay = int(hours) * int(rate)
print("Pay: {}".format(pay))