#https://leetcode.com/problems/container-with-most-water/submissions/

from sys import stdin
from typing import List
input = stdin.readline

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        all_areas = []
        while left < right:
            if height[left] < height[right]:
                all_areas.append((right - left) * height[left])
                left += 1
            else:
                all_areas.append((right - left) * height[right])
                right -= 1
        return max(all_areas)