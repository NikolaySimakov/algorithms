from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        i = 0

        while i < len(nums):
            s = str(nums[i])
            j = i + 1

            while j < len(nums) and nums[j] - nums[j-1] == 1:
                j += 1
            
            if j - 1 > i:
                s += '->' + str(nums[j - 1])
            
            res.append(s)
            i = j
        
        return res