#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 15:59
# @Author  : Shaniqua Qiu
# @File    : 703. 数据流中的第 K 大元素.py

# 2021-02-11 0.Daily Question
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest类：
#   KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
#   int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    # 小根堆中保留的一直是堆中的前 K 大的元素，堆的大小是 K，所以堆顶元素是第 K 大元素。
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]