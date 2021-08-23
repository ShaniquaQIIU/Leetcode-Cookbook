#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 19:10
# @Author  : Shaniqua Qiu
# @File    : 457. 环形数组是否存在循环.py


# https://leetcode-cn.com/problems/circular-array-loop/
# 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：
# 如果 nums[i] 是正数，向前 移动 nums[i] 步
# 如果 nums[i] 是负数，向后 移动 nums[i] 步
# 因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。
# 数组中的 循环 由长度为 k 的下标序列 seq ：
# 遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# 所有 nums[seq[j]] 应当不是 全正 就是 全负
# k > 1
# 如果 nums 中存在循环，返回 true ；否则，返回 false 。

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        # x的下一个位置
        nxt = lambda x: (x + nums[x]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            slow = i
            fast = nxt(i)
            # 快慢指针
            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            # 访问过的置0
            while nums[i] > 0:
                tmp = nxt(i)
                nums[i] = 0
                i = tmp
        return False