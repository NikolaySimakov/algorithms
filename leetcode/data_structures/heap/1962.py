import heapq
from math import ceil
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr = []

        for pile in piles:
            heapq.heappush(arr, -pile)

        for _ in range(k):
            max_pile = heapq.heappop(arr)
            max_pile -= ceil(max_pile / 2)
            heapq.heappush(arr, max_pile)
        
        return -sum(arr)