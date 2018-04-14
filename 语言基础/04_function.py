#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用函数重写计算工作量的程序，两个参数( hours and rate)。
# Enter Hours: 45 Enter Rate: 10
def count_pay(hours1, rate1):
    if 0 < hours1 < 40:
        pay1 = hours1 * rate1
    elif hours1 > 40:
        pay1 = 40 * rate1 + (hours1 - 40) * rate1 * 1.5
    else:
        pay1 = 0
    return pay1


if __name__ == '__main__':
    hours = input("Enter Hours:")
    rate = input("Enter Rate:")
    try:
        hours = int(hours)
        rate = int(rate)
        pay = count_pay(hours, rate)
        print("Pay:{}".format(pay))
    except:
        print("Error, please enter numeric input")
