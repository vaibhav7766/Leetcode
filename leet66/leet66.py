# https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=math

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        digits.insert(0, 0)
        i = len(digits) - 1
        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        digits[i] += 1
        if digits[0] == 0:
            digits.pop(0)
        return digits