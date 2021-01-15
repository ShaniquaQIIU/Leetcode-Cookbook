#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 11:03
# @Author  : Shaniqua Qiu
# @File    : 104. 二叉树的最大深度.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
