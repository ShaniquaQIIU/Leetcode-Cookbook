#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 16:57
# @Author  : Shaniqua Qiu
# @File    : 326. 3的幂.py

# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res < n:
            res *=3
        return res==n

import math

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        num = math.log(n)/math.log(3)  # log函数只判断>0的数
        if (num-int(num))== 0  or (num-int(num)) >= 0.99999999999999:
            return True
        return False

if __name__ == '__main__':
    s = Solution2()
    s.isPowerOfThree(-3)