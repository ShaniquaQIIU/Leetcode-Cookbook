#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 15:59
# @Author  : Shaniqua Qiu
# @File    : 374猜数字大小.py


# 猜数字游戏的规则如下：
# 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/guess-number-higher-or-lower


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pick = 6
    if pick < num:
        return -1
    elif pick > num:
        return 1
    else:
        return 0

# 2022-07-18
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right-left)//2 + left
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1: # pick < num
                right = mid-1
            else:
                left = mid+1
        return None
