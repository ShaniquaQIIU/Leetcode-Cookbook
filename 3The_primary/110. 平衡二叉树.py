#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 17:44
# @Author  : Shaniqua Qiu
# @File    : 110. 平衡二叉树.py

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return left+1 if left>right else right+1

        return height(root) != -1
