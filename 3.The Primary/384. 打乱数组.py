#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 15:23
# @Author  : Shaniqua Qiu
# @File    : 384. 打乱数组.py

# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
# 实现 Solution class:
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = [x for x in self.nums]
        for i in range(len(nums)-1):
            rand = randint(i, len(nums)-1)
            nums[i], nums[rand] = nums[rand], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
