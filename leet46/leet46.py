#https://leetcode.com/problems/permutations/
from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

obj = Solution()
print(obj.permute([0,1]))