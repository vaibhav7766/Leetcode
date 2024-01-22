#https://leetcode.com/problems/palindrome-number/submissions/

import sys
input = sys.stdin.readline

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]