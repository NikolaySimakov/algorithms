from typing import List

class Solution:
    
    # trivial solution
    def rearrangeArray1(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 1):
            if nums[i-1] + nums[i+1] == 2 * nums[i]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
        
        for i in range(len(nums) - 2, 0, -1):
            if nums[i-1] + nums[i+1] == 2 * nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

        return nums
    
    # math solution
    # you know that if a, b < c or a, b > c => (a + b)/2 != c
    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 1):
            if (nums[i-1] < nums[i] < nums[i+1]) or (nums[i-1] > nums[i] > nums[i+1]):
                nums[i+1], nums[i] = nums[i], nums[i+1]
        
        return nums