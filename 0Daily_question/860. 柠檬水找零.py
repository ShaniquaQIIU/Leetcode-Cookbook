#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 06:54
# @Author  : Shaniqua Qiu
# @File    : 860. 柠檬水找零

# 每位顾客只买一杯柠檬水，然后向你付 5Study_plan 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5Study_plan 美元。
# 注意，一开始你手头没有任何零钱。
# 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        if not bills:
            return True

        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if ten < 1:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                else:
                    five -= 1
                    ten -= 1
            if five < 0: return False
        return True


class Solution:
    # 优化下判断逻辑
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        if not bills:
            return True

        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five -= 1
                ten += 1
            else:
                if ten > 0:
                    five -= 1
                    ten -= 1
                else:
                    five -= 3
            if five < 0: return False
        return True