# https://leetcode.com/problems/merge-k-sorted-lists/description/

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def create_ll(self, n, arr: List[int]) -> Optional[ListNode]:
        if n == 0:
            return None
        ll = ListNode(arr[0])
        temp = ll
        for i in range(1, n):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return ll

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            temp_list = []
            temp = i
            while temp:
                temp_list.append(temp.val)
                temp = temp.next
            l.append(temp_list)
        heap = list(heapq.merge(*l))
        ll = self.create_ll(len(heap), heap)
        return ll
