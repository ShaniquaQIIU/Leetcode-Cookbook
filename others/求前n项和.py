#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 12:41
# @Author  : Shaniqua Qiu
# @Site    :
# @File    : 20201127.py

# 输入n求前n项和 122333444455555  n=1输出1 n=5输出11
def sum_items(n):
    if n ==1:
        return 1
    i = 1
    while n>i:
        n = n-i
        i +=1
    return i*(i+1)*(2*i+1)/6 - i*(i-n)


if __name__ == "__main__":
    n=9
    print(sum_items(n))