#https://leetcode.com/problems/add-two-numbers/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        temp = l1
        while temp:
            s1 += str(temp.val)
            temp = temp.next
        s2 = ""
        temp = l2
        while temp:
            s2 += str(temp.val)
            temp = temp.next
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        result = num1 + num2
        result_str = str(result)[::-1]
        dummy = ListNode()
        current = dummy
        for digit in result_str:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next