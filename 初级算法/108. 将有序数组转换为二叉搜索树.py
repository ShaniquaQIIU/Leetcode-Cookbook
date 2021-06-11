#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 10:01
# @Author  : Shaniqua Qiu
# @File    : 108. 将有序数组转换为二叉搜索树.py

# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        tn = TreeNode(nums[mid])
        l1 = nums[:mid]
        l2 = nums[mid+1:]
        tn.left = self.sortedArrayToBST(l1)
        tn.right = self.sortedArrayToBST(l2)
        return tn