#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 18:45
# @Author  : Shaniqua Qiu
# @File    : 112. 路径总和.py

# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
# 叶子节点 是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.left is None and root.right is None:
            return targetSum-root.val == 0
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
