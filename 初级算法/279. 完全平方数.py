#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 15:48
# @Author  : Shaniqua Qiu
# @File    : 279. 完全平方数.py

# 给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


class Solution:
    ''' 四平方定理
    任何正整数都可以拆分成不超过4个数的平方和 ---> 答案只可能是1,2,3,4
    如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7) ---> 因此可以先看这个数是否满足上述公式，如果不满足，答案就是1,2,3了
    如果这个数本来就是某个数的平方，那么答案就是1，否则答案就只剩2,3了
    如果答案是2，即n=a^2+b^2，那么我们可以枚举a，来验证，如果验证通过则答案是2
    只能是3    '''
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return bool(a) + bool(b)
            a += 1
        return 3


class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step

    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value, self.step)


class Solution:
    ''' 广度优先搜索
    '''
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])

        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                if i == 0:
                    return new_vertex.step

                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)

        return -1


