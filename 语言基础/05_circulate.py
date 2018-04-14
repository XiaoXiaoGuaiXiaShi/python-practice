#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 让用户输入一组数，直到用户输入“done”。输入“done”后，显示这组数的个数、和、平均值。在用户输入数时，使用try和except检查输入是否是数值，如果不是，则输出错误信息，跳到下一次数据。
# 同样是以上输入要求，只是求最大值和最小值。
def print_info( a ):
    sum = 0
    j = 0
    print("个数：{}".format(len(a)))
    for i in range(len(a)):
        sum += a[i]
        j = len(a)
        avg = sum/j
    print("和：{}".format(sum))
    print("平均数：{}".format(avg))

def max(a):
    max_n = a[0]
    for i in range(len(a)):
        if a[i] > max_n:
            max_n = a[i]
        else:
            continue
    return max_n

def min(a):
    min_n = a[0]
    for i in range(len(a)):
        if a[i] < min_n:
            min_n = a[i]
        else:
            continue
    return min_n

if __name__ == '__main__':
    a = input("请输入这组数中的第一个数：")
    i = 0
    list = []
    b = []
    while(a != "done"):
        list.append(a)
        a = input("请输入这组数中的第{}个数：".format(i+2))
        i += 1
    for i in range(len(list)):
        try:
            b.append(int(list[i]))
        except:
            print("第{}个数不是数值".format(i+1))
    print_info(b)
    max_n = max(b)
    min_n = min(b)
    print("最大值：{}".format(max_n))
    print("最小值：{}".format(min_n))