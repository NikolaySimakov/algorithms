from typing import List

'''
Solution O(N^2)

_, _, nums[i], _, _, nums[l] -> , _, _, <- nums[r], _, _

On every i++ iteration getting l, r indexes and then 
check if sum nums[i] + nums[l] + nums[r] closest to target value

if nums[i] + nums[l] + nums[r] > target: r--
else if nums[i] + nums[l] + nums[r] < target: l++
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closestSum = None

        for i in range(n):
            l, r = i + 1, n - 1
            
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res == target:
                    return target
                elif res < target:
                    l += 1
                else:
                    r -= 1
            
                if closestSum is None or abs(target - res) <= abs(closestSum - target):
                    closestSum = res
        
        return closestSum