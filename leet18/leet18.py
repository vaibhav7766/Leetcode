# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def ksum(self, k: int, start: int, target: int, nums: List[int]) -> int:
        if k != 2:
            return self.ksum(k - 1, start + 1, target - nums[start], nums)

        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append(quad + [nums[left], nums[right]])

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        global res
        global quad
        res, quad = [], []
        self.ksum(4, 0, target, nums)
        return res
