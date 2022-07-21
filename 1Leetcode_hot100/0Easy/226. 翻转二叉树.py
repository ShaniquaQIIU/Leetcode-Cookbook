#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 17:56
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/invert-binary-tree/
# @File    : 226. 翻转二叉树.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(right)
        return root
