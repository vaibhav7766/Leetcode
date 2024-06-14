class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack or hashmap[i] != stack.pop():
                    return False
        return not stack