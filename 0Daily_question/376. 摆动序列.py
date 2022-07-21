#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 09:20
# @Author  : Shaniqua Qiu
# @File    : 376. 摆动序列

# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
# 第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res, pre_diff, cur_diff = 1, 0, 0
        for i in range(1, len(nums), 1):
            cur_diff = nums[i] - nums[i-1]
            # 出现波峰或波谷
            if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
                res += 1
                pre_diff = cur_diff
        return res
