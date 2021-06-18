#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 11:54
# @Author  : Shaniqua Qiu
# @File    : 98. 验证二叉搜索树.py

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.search(root)

    def search(self, root, left=float('-inf'), right=float('inf')):
        if not root:
            return True
        return left < root.val < right \
               and self.search(root.left, left, root.val) \
               and self.search(root.right, root.val, right)