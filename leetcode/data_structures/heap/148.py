import heapq
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        heap = []
        res = ListNode()
        tail = res

        while head:
            heapq.heappush(heap, head.val)
            head = head.next
        
        while heap:
            v = heapq.heappop(heap)
            tail.next = ListNode(val=v)
            tail = tail.next
        
        return res.next