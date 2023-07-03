from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        '''
        Leetcode 1248
        Use prefix sum array to define count of odd numbers in prefix
        Use hashmap to count all need prefixes
        
        Example:
        
        1 2 3 4 5 6 7 8 9 -> 1 1 2 2 3 3 4 4 5
        k = 2 => map {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 1} -> 2 + 4 + 4 + 2 = 12
        '''

        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]%2

        for i in range(1, n):
            prefix[i] += prefix[i-1] + nums[i]%2
        
        count = 0
        prefix = prefix
        mp = {0:1}

        for i in range(n):
            if prefix[i] - k >= 0:
                count += mp[prefix[i] - k]
            if prefix[i] in mp: mp[prefix[i]] += 1
            else: mp[prefix[i]] = 1
        
        return count