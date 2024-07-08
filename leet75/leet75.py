# https://leetcode.com/problems/sort-colors/description/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start, end, mid = 0, n - 1, 0
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1