#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 09:35
# @Author  : Shaniqua Qiu
# @File    : Q18 水果酥饼日.py


def checkValid(n, pre, arr, square):
    # 全部分割结束
    if n == len(arr):
        # 与第一块酥饼凑成平方数
        if (1 + pre) in square:
            print(arr)
            return True
    else:
        for i in range(1, n + 1):
            if i in arr:
                continue
            if ((i + pre) in square) and (checkValid(n, i, arr + [i], square)):
                return True
    return False


if __name__ == '__main__':
    n = 7
    while True:
        # 事先对于每一个 n 计算平方数集合
        square = [x * x for x in range(1, n)]
        if checkValid(n, 1, [1], square):
            break
        n += 1