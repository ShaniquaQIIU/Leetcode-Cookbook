#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 11:56
# @Author  : Shaniqua Qiu
# @File    : 70. 爬楼梯.py

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 到第n-1个台阶的走法 + 第n-2个台阶的走法 = 到第n个台阶的走法
# 超时
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = {1: 1, 2: 2}
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [1,2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        pre,cur = 1, 2
        for i in range(3,n+1):
            tmp = pre
            pre = cur
            cur = tmp + cur
        return cur
