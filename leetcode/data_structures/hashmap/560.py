from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = count = 0
        d = defaultdict(int)
        d[0] = 1

        for i in range(n):
            prefix_sum += nums[i]
            if (prefix_sum - k) in d:
                count += d[prefix_sum - k]
            d[prefix_sum] = d[prefix_sum] + 1 if prefix_sum in d else 1

        return count