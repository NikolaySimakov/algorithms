from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            nums[l] = nums[r]
            if nums[r] != val:
                l += 1
        
        return l