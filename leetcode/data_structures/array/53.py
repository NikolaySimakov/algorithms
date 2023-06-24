from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mx = nums[0]
        mn = min(0, nums[0])

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            mx = max(mx, nums[i] - mn)
            mn = min(mn, nums[i])
        
        return mx
