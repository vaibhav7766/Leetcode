# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        ptr1, ptr2 = list1, list2
        while ptr1 is not None and ptr2 is not None:
            if ptr2.val >= ptr1.val:
                temp.next = ptr1
                ptr1 = ptr1.next
            else:
                temp.next = ptr2
                ptr2 = ptr2.next
            temp = temp.next

        if ptr1 is not None:
            temp.next = ptr1

        if ptr2 is not None:
            temp.next = ptr2

        return head.next
