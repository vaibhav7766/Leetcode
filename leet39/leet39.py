#https://leetcode.com/problems/combination-sum/
from typing import List
from sys import stdin

input = stdin.readline

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]] | None:
        if len(candidates) == 0:
            return []
        if target == 0:
            return [[]]
        res = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            for j in self.combinationSum(candidates[i:], target - candidates[i]):
                res.append([candidates[i]] + j)
        return res