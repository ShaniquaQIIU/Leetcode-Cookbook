#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/11 17:42
# @Author  : Shaniqua Qiu
# @File    : 1984. 学生分数的最小差值.py

# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
# 返回可能的 最小差值 。
# 链接：https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

from typing import List


#  滑动窗口
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans