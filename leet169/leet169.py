#https://leetcode.com/problems/majority-element/description/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        for i in nums:
            if i == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = i
                    count = 1
        return majority