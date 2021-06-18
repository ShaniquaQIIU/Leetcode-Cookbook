#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 15:00
# @Author  : Shaniqua Qiu
# @File    : 1052. 爱生气的书店老板.py

# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

from typing import List

# 首先算出所有不生气时间段的顾客数；再利用滑动窗口算出连续不生气时间的最大顾客值
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res, ans, max_customers = 0, 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0
            ans += customers[i]
            max_customers = max(max_customers, ans)
            if i >= X-1:    # 方便计算连续的时间段
                ans -= customers[i-(X-1)]
        return res+max_customers
