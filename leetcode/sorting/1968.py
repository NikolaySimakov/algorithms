from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 1):
            if nums[i-1] + nums[i+1] == 2 * nums[i]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
        
        for i in range(len(nums) - 2, 0, -1):
            if nums[i-1] + nums[i+1] == 2 * nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

        return nums