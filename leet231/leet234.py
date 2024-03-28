#https://leetcode.com/problems/power-of-two/
from sys import stdin
input = stdin.readline

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return (not n & (n-1))

obj = Solution()
print(obj.isPowerOfTwo(536870912))