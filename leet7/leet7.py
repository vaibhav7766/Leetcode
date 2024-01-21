#https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -2**31
        
        isnegative = False
        if x < 0:
            isnegative = True
            x = abs(x)
        
        rev_str = str(x)[::-1].lstrip('0')
        
        if not rev_str:
            return 0 
        
        rev = int(rev_str) if not isnegative else -int(rev_str)
        
        if rev not in range(MIN_INT, MAX_INT + 1):
            return 0
        else:
            return rev