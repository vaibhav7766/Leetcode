from typing import List

class Solution:
    def bs(self, arr: List[int], left: int, right: int, target: int) -> int:
        mid = (left + right) // 2
        if left > right:
            return -1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.bs(arr, mid + 1, right, target)
        else:
            return self.bs(arr, left, mid - 1, target)
        return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) - 1, target)