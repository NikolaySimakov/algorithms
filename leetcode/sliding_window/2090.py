from typing import List

'''
K Radius Subarray Averages
Sliding window as radius of index with length k
'''

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        window_sum, window_size = sum(nums[:2*k]), 2*k + 1

        if window_size == 0:
            return nums

        for i in range(2*k, n):
            window_sum += nums[i]
            mid = i - window_size//2
            res[mid] = window_sum // window_size
            window_sum -= nums[i - window_size + 1]
        
        return res