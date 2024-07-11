# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def len_of_ll(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        return length

    def remove_element(self, head: Optional[ListNode], k: int):
        if k == 0:
            return head.next
        temp = head
        pos = 0
        while pos < k - 1:
            temp = temp.next
            pos += 1
        temp.next = temp.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.len_of_ll(head)
        t = length - n
        temp1 = head
        return self.remove_element(temp1, t)

# One-pass solution

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         temp = ListNode(0, head)
#         first = temp
#         second = temp
#         for _ in range(n + 1):
#             first = first.next
#         while first:
#             first = first.next
#             second = second.next

#         second.next = second.next.next
#         return temp.next
