#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 15:03
# @Author  : Shaniqua Qiu
# @File    : 102. 二叉树的层序遍历.py

# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            res.append([i.val for i in queue])
            child = []
            for i in queue:
                if i.left:
                    child.append(i.left)
                if i.right:
                    child.append(i.right)
            queue = child
        return res
