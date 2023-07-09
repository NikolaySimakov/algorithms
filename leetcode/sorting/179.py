from functools import cmp_to_key
from typing import List

class Solution:
    
    # easy to understand solution
    def largestNumberSimple(self, nums: List[int]) -> str:
        nums = list(map(str, nums)) # nums from int to string
        max_number = ""
        
        while len(nums) > 0:
            curr_max = "0"
            for num in nums:
                if num + curr_max > curr_max + num:
                    curr_max = num
            max_number += curr_max
            nums.remove(curr_max)
            
        return max_number if max_number[0] != "0" else "0"
    
    # using functools.cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums)) # nums from int to string
        
        def compare(a, b):
            return -1 if a + b > b + a else 1
        
        nums = sorted(nums, key=cmp_to_key(compare)) # sort nums by key compare function
        return str(int(''.join(nums))) # remove leading zeros