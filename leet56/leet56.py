# https://leetcode.com/problems/merge-intervals/description/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            last = merged[-1]
            if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged
