#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 09:31
# @Author  : Shaniqua Qiu
# @File    : 103. 二叉树的锯齿形层序遍历.py

# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 2020-12-22 这题不会 树是硬伤

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        pass
