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
        deque = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            if deque and deque[0] <= i-k:
                deque.popleft()
            while deque and nums[deque[-1]] < num:  # 移除比当前数小的数字索引
                deque.pop()
            deque.append(i)
            if i >= k-1:
                ans.append(nums[deque[0]])
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = s.maxSlidingWindow(nums, k)
    print(res)