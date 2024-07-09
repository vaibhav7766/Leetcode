# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if not digits:
            return []
        elif len(digits) == 1:
            return list(hashmap[int(digits[0])])
        else:
            return [i+j for i in self.letterCombinations(digits[0:-1]) for j in hashmap[int(digits[-1])]]