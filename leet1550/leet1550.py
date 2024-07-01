# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = False
        count = 0
        for i in arr:
            if i % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                flag = True
                break
        return flag
