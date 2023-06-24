from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        s = ListNode(next=head)
        fast = slow = s
        counter = 0

        while fast.next:
            if counter > n - 1:
                slow = slow.next
            
            fast = fast.next
            counter += 1
        
        slow.next = slow.next.next if slow.next else None
        return s.next