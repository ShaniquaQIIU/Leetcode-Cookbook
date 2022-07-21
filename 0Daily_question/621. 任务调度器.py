#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5Study_plan 18:16
# @Author  : Shaniqua Qiu
# @File    : 621. 任务调度器.py

# 2020-12-05 题目
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 你需要计算完成所有任务所需要的 最短时间 。

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 总排队时间 = (单任务最大个数 - 1) * (n + 1) + 剩余的任务数
        task_hash = {}
        for i in tasks:
            task_hash[i] = task_hash.get(i, 0) + 1

        task_max = max(task_hash.values())
        rest_task = 0
        for key in task_hash.keys():
            if task_hash[key] == task_max:
                rest_task += 1
        res = (task_max-1) * (n+1) + rest_task

        return res if res >= len(tasks) else len(tasks)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,3,3,4,5]
    n = 2
    s.leastInterval(nums, 2)

