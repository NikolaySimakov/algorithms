from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        tail = head
        stack = []

        while tail:
            stack.append(tail)
            tail = tail.next

        tail = head
        s = (len(stack))//2

        while s > 0:
            top = stack.pop()
            temp = tail.next
            tail.next = top
            top.next = temp
            tail = temp
            s -= 1

        tail.next = None
