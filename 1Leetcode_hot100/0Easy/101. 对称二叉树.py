#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 14:12
# @Author  : Shaniqua Qiu
# @File    : 101. 对称二叉树.py

# 给定一个二叉树，检查它是否是镜像对称的。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.search(root.left, root.right)

    def search(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.search(root1.left, root2.right) and self.search(root2.left, root1.right)
        return False

