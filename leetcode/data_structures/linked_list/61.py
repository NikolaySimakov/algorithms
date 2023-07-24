from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        n = 1
        fast = head
        while fast.next:
            n += 1
            fast = fast.next
        
        fast.next = head

        k %= n

        for _ in range(1, n - k):
            head = head.next

        temp = head.next
        head.next = None
        
        return temp
