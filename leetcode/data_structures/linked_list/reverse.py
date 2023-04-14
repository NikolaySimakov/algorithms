from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        save = ListNode()
        tail = save

        while head:
            a = save.next
            save.next = ListNode()
            save.next.val = head.val
            save.next.next = a

            # next step
            head = head.next

        return save.next
