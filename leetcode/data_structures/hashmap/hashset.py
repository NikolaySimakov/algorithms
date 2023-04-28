# Task 705

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.starts = []
        self.step = 500

        for i in range(0, 1000001, self.step):
            self.starts.append(ListNode())

    def add(self, key: int) -> None:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.val > key:
                node = ListNode(val=key, next=p.next)
                p.next = node
                break
            if p.next.val == key:
                break

            p = p.next

    def remove(self, key: int) -> None:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.val > key:
                break
            if p.next.val == key:
                p.next = p.next.next
                break

            p = p.next

    def contains(self, key: int) -> bool:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.val > key:
                return False
            if p.next.val == key:
                return True

            p = p.next


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
