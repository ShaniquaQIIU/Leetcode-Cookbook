#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 15:57
# @Author  : Shaniqua Qiu
# @File    : 230. 二叉搜索树中第K小的元素.py

# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉搜索数 左子树的值总小于根节点
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []
        def midsearch(root):
            if root:
                midsearch(root.left)
                l.append(root.val)
                midsearch(root.right)
        midsearch(root)
        return l[k - 1]
