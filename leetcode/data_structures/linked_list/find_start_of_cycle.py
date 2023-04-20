from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()

        while head:
            if head in nodes:
                return head
            else:
                nodes.add(head)

            head = head.next

        return None
