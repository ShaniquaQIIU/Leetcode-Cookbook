#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 09:55
# @Author  : Shaniqua Qiu
# @File    : Q26 高效的立体停车场.py

# f(n,m)= 8n−11  n=m
#         2(n+m)+4max(n,m)−13   n<>m

class Solution:
    def parkSteps(self, n: int, m: int) -> int:
        if m == n:
            return 8*n-11
        else:
            return 2*(n+m)+4*max(n,m)-13