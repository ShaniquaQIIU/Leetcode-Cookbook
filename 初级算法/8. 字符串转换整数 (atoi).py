#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:09
# @Author  : Shaniqua Qiu
# @File    : 8. 字符串转换整数 (atoi).py

# 本题中的空白字符只包括空格字符 ' ' 。
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为[−2**31,2**31− 1]。
# 如果数值超过这个范围，请返回 INT_MAX (2**31− 1) 或INT_MIN (−2**31) 。
# 假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0 。


import re


class Solution:
    def myAtoi(self, s: str) -> int:
        num = re.findall('^[\+\-]?\d+', s.strip())
        # print(num)
        return min(max(int(*num), -2**31), 2**31 - 1)


if __name__ == '__main__':
    s = Solution()
    res = s.myAtoi(str("words and 987"))
    print(res)
