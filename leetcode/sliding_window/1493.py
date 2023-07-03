from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # using sliding window 
        # this task is similar to 1004

        l = 0
        max_length = 0
        flag = nums[0] == 0

        for r in range(1, len(nums)):
            if nums[r] == 0:
                if flag:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    flag = True
            
            max_length = max(max_length, r - l)
        
        return max_length