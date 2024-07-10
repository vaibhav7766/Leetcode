# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_ll(self, ll: ListNode) -> list:
        s = ""
        temp = ll
        while temp:
            s += str(temp.val)
            temp = temp.next
        return s

    def str_to_ll(self, s: str) -> ListNode:
        if not s:
            return None
        ll = ListNode(s[0])
        temp = ll
        for i in range(1, len(s)):
            temp.next = ListNode(s[i])
            temp = temp.next
        return ll

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = int(self.print_ll(l1)[::-1])
        s2 = int(self.print_ll(l2)[::-1])
        ans = str(s1 + s2)[::-1]

        return self.str_to_ll(ans)
