# Leetcode 706

class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.starts = []
        self.step = 500

        for i in range(0, 1000001, self.step):
            self.starts.append(ListNode())

    def put(self, key: int, value: int) -> None:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.key > key:
                node = ListNode(key=key, val=value, next=p.next)
                p.next = node
                break
            if p.next.key == key:
                p.next.val = value
                break

            p = p.next

    def get(self, key: int) -> int:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.key > key:
                return -1
            if p.next.key == key:
                return p.next.val

            p = p.next

    def remove(self, key: int) -> None:
        p = self.starts[key//self.step]

        while True:
            if not p.next or p.next.key > key:
                break
            if p.next.key == key:
                p.next = p.next.next
                break

            p = p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
