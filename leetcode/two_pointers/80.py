from typing import List

'''
Based on Leetcode 26 solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1

where [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] -> [1, 2, 3, 4]
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        '''
        It's a part case of Leetcode 26 task 
        but in this task you need remove only 
        if count of numer in array > 2
        
        so, we can use flag to check it
        '''
        
        l = 0
        flag = False

        for r in range(1, len(nums)):
            if nums[r] == nums[l]:
                # the left index will lag behind the right index 
                # by the number of extra numbers
                if not flag:
                    l += 1
                    nums[l] = nums[r]
                    flag = True
            else:
                l += 1
                nums[l] = nums[r]
                flag = False

        return l + 1