#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 10:12
# @Author  : Shaniqua Qiu
# @File    : 204. 计数质数.py

# 2020-12-03 题目 注意审题判断的是小于n的算法
# 统计所有小于非负整数 n 的质数的数量。

# 普通算法, 质数不能被除本身外的其他数整除
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        count = 0
        for x in range(2,n):
            for y in range(2,int(x**0.5)+1):
                if x % y == 0:
                    break
            else:
                count +=1
        return count


# 厄拉多塞素数筛选法
# 先将2－N的各数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
# 第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
# 现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……
# 依次类推，一直到所有小于N的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 N的素数。
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        l = list(range(1,n))
        l[0] = 0
        for i in range(2,n):
            if l[i-1] != 0 :  # 从2开始判断, 跳过倍数，只用质数判断
                for j in range(i*2,n,i):
                    l[j-1] = 0
        result = [x for x in l if x != 0]
        return len(result)
