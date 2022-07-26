#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 17:54
# @Author  : Shaniqua Qiu
# @File    : 441排列硬币.py


# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/arranging-coins

# total= k×(k+1)/2
# k = (−1+(√8n+1))/2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow((8*n+1), 0.5)-1)//2)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (right+left+1)//2
            print(mid)
            print(mid*(mid+1))
            if mid*(mid+1) <= 2*n:
                left = mid
            else:
                right = mid-1
        return left


if __name__ == '__main__':
    s = Solution()
    res = s.arrangeCoins(8)
    print(res)