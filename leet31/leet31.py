# https://leetcode.com/problems/next-permutation/description/
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k = n - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        if k == -1:
            nums.reverse()
            return
        l = k + 1
        while l < n and nums[l] > nums[k]:
            l += 1
        l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = reversed(nums[k + 1:])