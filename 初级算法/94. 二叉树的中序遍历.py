#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 15:36
# @Author  : Shaniqua Qiu
# @File    : 94. 二叉树的中序遍历.py

# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历 左子树->根节点->右子树
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
