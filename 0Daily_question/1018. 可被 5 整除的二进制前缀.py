#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 09:50
# @Author  : Shaniqua Qiu
# @File    : 1018. 可被 5Study_plan 整除的二进制前缀.py

# 给定由若干0和1组成的数组 A。我们定义N_i：从A[0] 到A[i]的第 i个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
# 返回布尔值列表answer，只有当N_i可以被 5整除时，答案answer[i] 为true，否则为 false。
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res, num = [], 0
        for i in range(len(A)):
            num <<= 1
            num += A[i]
            res.append(num%5==0)
        return res
