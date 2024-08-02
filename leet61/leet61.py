# https://leetcode.com/problems/rotate-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1

        temp.next = head

        k = k % length
        steps_to_new_head = length - k
        temp = head

        for _ in range(steps_to_new_head - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        return new_head
