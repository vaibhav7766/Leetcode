#https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        maxlen:int = 0
        start = -1
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
            d[s[i]] = i
            maxlen = max(maxlen, i - start)
        return maxlen