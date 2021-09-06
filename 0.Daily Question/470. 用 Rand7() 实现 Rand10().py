#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 19:16
# @Author  : Shaniqua Qiu
# @File    : 470. 用 Rand7() 实现 Rand10().py

# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 不要使用系统的 Math.random() 方法。


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            seed = (rand7() - 1) * 7 + rand7() - 1
            if seed >= 1 and seed <= 10:
                return seed