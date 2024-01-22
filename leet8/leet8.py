#https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        res = 0
        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)

        res *= sign
        return max(INT_MIN, min(INT_MAX, res))