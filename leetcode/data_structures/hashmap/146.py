from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.keys_count = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
        elif len(self.cache) == self.capacity:
            self.cache.popitem()

        self.cache[key] = value
        self.cache.move_to_end(key, last=False)