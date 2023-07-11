from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = count = 0
        d = {0 : 1}

        for i in range(n):
            prefix_sum += nums[i]
            if (prefix_sum - k) in d:
                count += d[prefix_sum - k]

            if prefix_sum in d: d[prefix_sum] += 1
            else: d[prefix_sum] = 1

        return count