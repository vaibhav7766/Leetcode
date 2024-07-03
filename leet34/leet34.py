# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        target_index = -1
        start_index, end_index = -1, -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                target_index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if target_index == -1:
            return [start_index, end_index]

        start_index = target_index
        while start_index > 0 and nums[start_index] == nums[start_index - 1]:
            start_index -= 1

        end_index = target_index
        while end_index < n - 1 and nums[end_index] == nums[end_index + 1]:
            end_index += 1

        return [start_index, end_index]
