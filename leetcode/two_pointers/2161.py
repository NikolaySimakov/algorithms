from typing import List

'''

Two approaches:
 - using simulation
 - using two pointers
 
'''

class Solution:
    def pivotArraySimulation(self, nums: List[int], pivot: int) -> List[int]:
        arr1 = []
        arr2 = []
        arr3 = []

        for num in nums:
            if num > pivot:
                arr1.append(num)
            elif num < pivot:
                arr2.append(num)
            else:
                arr3.append(num)
        
        return arr2 + arr3 + arr1
    
    def pivotArrayTwoPointers(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        for i in range(n):
            
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1
            
            if nums[n - i - 1] > pivot:
                res[r] = nums[n - i - 1]
                r -= 1
        
        while l <= r:
            res[l] = pivot
            l += 1
        
        return res
