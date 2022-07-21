#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 17:57
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/merge-two-binary-trees/
# @File    : 617. 合并二叉树.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val = root1.val+root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
