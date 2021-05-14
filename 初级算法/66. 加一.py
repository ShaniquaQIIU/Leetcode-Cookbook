# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 06:49
# @Author  : Shaniqua Qiu
# @File    : 66. 加一.py

# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

from typing import List


# 2020-12-15
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, index, total = 0, len(digits), 0
        if index == 0: return
        for i in digits:
            num += i * (10 ** (index - 1))
            index -= 1
        len1 = len(str(num))
        num += 1  # 数字加1
        len2 = len(str(num))
        add_digits = []
        if len1 != len2:
            total = len(digits)
        else:
            total = len(digits) - 1
        while index <= total:
            digit = int(num % 10)
            num = int(num // 10)  # 整除
            add_digits.append(digit)
            index += 1
        return add_digits[::-1]  # 倒序


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:  # 如果满十进位到数组第一个，则数组需要增加一位
                    digits = [1] + digits
            else:
                digits[i] += 1  # 不等于9就终止循环结束
                break
        return digits


# 2021-05-13
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


if __name__ == "__main__":
    s = Solution2()
    digits = [0, 9]
    res = s.plusOne(digits)
    print(res)