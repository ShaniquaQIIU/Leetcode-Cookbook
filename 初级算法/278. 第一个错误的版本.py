#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 17:51
# @Author  : Shaniqua Qiu
# @File    : 278. 第一个错误的版本.py

# 给定 n = 5，并且 version = 4 是第一个错误的版本。
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5)-> true
# 调用 isBadVersion(4)-> true
# 所以，4 是第一个错误的版本。

class Solution:
    def firstBadVersion(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            mid = low + (high-low)//2
            if self.isBadVersion(mid):
                high = mid   # 查找区间[low, mid]
            else:
                low = mid + 1    # 查找区间[mid+1, high]
        return high

    def isBadVersion(self, n):
        return n >= 3

if __name__ == '__main__':
    s = Solution()
    res = s.firstBadVersion(15)
    print(res)
