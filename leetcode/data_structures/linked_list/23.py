from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:

    '''
    Solution using mergeTwoLists function.
    Create one ListNode and merge with it every ListNode from lists.
    '''

    def mergeTwoLists(self, l1, l2) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        merged = lists[0]
        for l in lists[1:]:
            merged = self.mergeTwoLists(merged, l)
        return merged


class Solution2:

    '''
    TODO: Solve this task using heap/queue
    '''

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass
