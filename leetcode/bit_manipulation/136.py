from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x
    
    # One line solution
    def singleNumberOneLine(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a^b, nums)