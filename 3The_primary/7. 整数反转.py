#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 19:11
# @Author  : Shaniqua Qiu
# @File    : 7. 整数反转.py

import math

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
class Solution1:
    def reverse(self, x: int) -> int:
        n, num = [], ''
        if x==0:
            return 0
        n[:] = list(str(x))[::-1]
        print(n)
        if n[-1] == '-':
            num += '-'
            num += ''.join(n[:-1])
        else:
            num += ''.join(n)
        return int(num) if -2**31< int(num) <2**31-1 else 0


class Solution2:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        res, x = 0, abs(x)
        while x != 0:
            res = res*10+x%10
            x //= 10
        return res*flag if  -2**31< res <2**31-1 else 0


if __name__ == '__main__':
    s = Solution2()
    res = s.reverse(-233333333)
    print(res)