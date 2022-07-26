#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 17:46
# @Author  : Shaniqua Qiu
# @File    : 278第一个错误的版本.py


# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/first-bad-version


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 3


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return right

