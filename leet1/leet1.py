# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        for index, num in enumerate(nums):
            aim = target - num
            if aim in hashmap and hashmap[aim] != index:
                return [index, hashmap[aim]]
        return []
