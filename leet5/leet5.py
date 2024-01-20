#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s[:]==s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        l = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i: j]
                if self.isPalindrome(sub):
                    if len(sub) > max_len:
                        max_len = len(sub)
                        l.append(sub)
        l = list(filter(lambda s: True if len(s) == max_len else False, l))
        return l[0]

'''
class Solution:
    @staticmethod
    def get_updated_string(s):
        sb = ''
        for i in range(0, len(s)):
            sb += '#' + s[i]
        sb += '#'
        return sb

    def longestPalindrome(self, s: str) -> str:
        updated_string = Solution.get_updated_string(s)
        length = 2 * len(s) + 1
        p = [0] * length
        c = 0
        r = 0
        maxLength = 0
        position = -1
        for i in range(0, length):
            mirror = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
            a = i + (1 + p[i])
            b = i - (1 + p[i])
            while a < length and b >= 0 and updated_string[a] == updated_string[b]:
                p[i] += 1
                a += 1
                b -= 1
            if i + p[i] > r:
                c = i
                r = i + p[i]
            if maxLength < p[i]:
                maxLength = p[i]
                position = i
        offset = p[position]
        result = ''
        for i in range(position - offset + 1, position + offset):
            if updated_string[i] != '#':
                result += updated_string[i]
        return result

'''
