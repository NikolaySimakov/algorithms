from typing import List

class Solution:
    
    # trivial solution O(nlog(n))
    def findUnsortedSubarraySimple(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        l, r = 0, n-1
    
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                break
            else:
                l += 1
        
        for i in range(n):
            if nums[n-i-1] != sorted_nums[n-i-1]:
                break
            else:
                r -= 1
        
        return max(0, r - l + 1)

    # O(n)
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