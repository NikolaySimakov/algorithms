from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        max_length = 0

        while r < len(nums):
            if nums[r] == 0:
                if k == 0:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    k -= 1
            max_length = max(max_length, r - l + 1)
            r += 1
        
        return max_length