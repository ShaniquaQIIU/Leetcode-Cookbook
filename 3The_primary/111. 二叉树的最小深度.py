#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 18:36
# @Author  : Shaniqua Qiu
# @File    : 111. 二叉树的最小深度.py

# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right: # 当有左右两个子节点取最小
            return 1+min(left, right)
        else:  #当有左子节点或右子节点，则单侧为最小路径
            return 1+left+right
