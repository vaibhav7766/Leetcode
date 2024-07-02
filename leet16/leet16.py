# https://leetcode.com/problems/3sum-closest/

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float("inf")
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if abs(total_sum - target) < abs(close_sum - target):
                    close_sum = total_sum
                if total_sum == target:
                    return total_sum
                elif total_sum > target:
                    right -= 1
                else:
                    left += 1
        return close_sum
