from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_min, cur_max = nums[-1], nums[0] # pointers
        start, end = 0, -1

        for i in range(n-2, -1, -1):
            if cur_min >= nums[i]:
                cur_min = nums[i]
            else:
                start = i
        
        for i in range(1, n):
            if cur_max <= nums[i]:
                cur_max = nums[i]
            else:
                end = i
        
        if start <= end:
            return end - start + 1
        return 0