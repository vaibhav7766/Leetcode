#https://leetcode.com/problems/xor-queries-of-a-subarray/

from sys import stdin
from typing import List
input = stdin.readline

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_xor = [0] * (n)
        prefix_xor[0] = arr[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i]
        
        ans = []
        for l,r in range(queries):
            if l == 0:
                temp = prefix_xor[r]
            else:
                temp = prefix_xor[r] ^ prefix_xor[l-1]
            ans.append(temp)
        return ans