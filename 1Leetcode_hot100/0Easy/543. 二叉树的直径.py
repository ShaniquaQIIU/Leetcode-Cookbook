#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 17:48
# @Author  : Shaniqua Qiu
# @File    : 543. 二叉树的直径.py

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans  = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(self.ans, l+r+1)  # 返回
            return max(l, r)+1   # 返回这个节点为根的子节点深度

        dfs(root)
        return self.ans-1
