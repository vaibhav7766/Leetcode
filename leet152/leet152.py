# https://leetcode.com/problems/maximum-product-subarray/description/
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_prod = 1
        suffix_prod = 1
        ans = nums[0]
        for i in range(n):
            prefix_prod = prefix_prod == 0 and 1 or prefix_prod
            suffix_prod = suffix_prod == 0 and 1 or suffix_prod
            prefix_prod *= nums[i]
            suffix_prod *= nums[n - 1 - i]
            ans = max(ans, max(prefix_prod, suffix_prod))
        return ans
