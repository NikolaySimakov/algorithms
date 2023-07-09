from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums)) # nums from int to string
        
        def compare(a, b):
            return -1 if a + b > b + a else 1
        
        nums = sorted(nums, key=cmp_to_key(compare)) # sort nums by key compare function
        res = ''.join(nums)
        return str(int(res))