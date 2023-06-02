import heapq
from typing import List


class Solution:
    
    # best
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]

    # more memory, without heap pop
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
    
    # trivial solution (sorting - O(n*log(n)))
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
    
    