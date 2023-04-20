from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head:
            if head not in nodes:
                nodes.add(head)
            else:
                return True
            head = head.next

        return False
