from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head:
            if head in nodes:
                return True
            else:
                nodes.add(head)

            head = head.next

        return False
