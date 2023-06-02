from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = list(reversed(sorted(list(dict(Counter(nums)).items()), key=lambda x: x[1])))
        return [i for i, _ in arr[:k]]
    
# Example
s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k))