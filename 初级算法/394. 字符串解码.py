#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 20:57
# @Author  : Shaniqua Qiu
# @File    : 394. 字符串解码.py

# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, count = [], "", 0
        for i in s:
            if i == '[':
                stack.append([res, count])
                res, count = "", 0
            elif i == ']':
                last_res, cur_count = stack.pop()
                res = last_res + cur_count*res
            elif "0" <= i and i <= "9":
                count = count*10 + int(i)
            else:
                res += i
        return res


# 2021-06-10 dfs
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            res, count = "", 0
            while i < len(s):
                if s[i] == '[':
                    last_res, i = dfs(s, i+1)
                    res += count*last_res
                    count = 0
                elif s[i] == ']':
                    return res, i
                elif "0" <= s[i] <= "9":
                    count = count*10 + int(s[i])
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)