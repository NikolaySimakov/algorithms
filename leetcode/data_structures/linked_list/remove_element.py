from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(val=0, next=head)
        tail = dummy

        while tail.next:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next

        return dummy.next
