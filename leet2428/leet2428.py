# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_sum = -float("inf")
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                cur_sum = (
                    grid[i - 1][j - 1]
                    + grid[i - 1][j]
                    + grid[i - 1][j + 1]
                    + grid[i][j]
                    + grid[i + 1][j - 1]
                    + grid[i + 1][j]
                    + grid[i + 1][j + 1]
                )
                max_sum = max(max_sum, cur_sum)
        return max_sum
