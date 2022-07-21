#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/2 11:01
# @Author  : Shaniqua Qiu
# @File    : 239. 滑动窗口最大值.py

# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

from typing import List
import collections


# 过于暴力，超过时间限制
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        ans = []
        for i in range(n-k+1):
            tmp = max(nums[i:i+k])
            ans.append(tmp)
        return ans


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        deque, res = [], []
        for i, num in enumerate(nums):
            if deque and deque[0] <= i-k:  # 移出非当前窗口的数据
                deque.pop(0)
            while deque and nums[deque[-1]] < num:  # 移出比当前数小的索引
                deque.pop()
            deque.append(i)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res


# 2021-10-15
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []  # 判空
        hp, res = [], []
        for i, v in enumerate(nums):
            while hp and hp[0][1] <= i-k:  # 移出非当前窗口的数据
                heapq.heappop(hp)
            heapq.heappush(hp, [-v, i])  # python是小顶堆，存负值转换为'大顶堆'
            if i >= k-1:  # 最大值存入结果数组
                res.append(-heapq[0][0])  # 再转回正值
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = s.maxSlidingWindow(nums, k)
    print(res)