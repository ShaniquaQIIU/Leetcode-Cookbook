#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 17:39
# @Author  : Shaniqua Qiu
# @File    : 338. 比特位计数.py

# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            if i & 1 == 0:    # i % 2 == 0
                res.append( res[i//2])
            else:
                res.append( res[i-1] +1)
        return res
