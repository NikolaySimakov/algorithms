from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = 0

        while True:

            if len(nums) == 1:
                if nums[0] == target:
                    return index
                else:
                    return -1

            l1 = len(nums)//2

            if nums[l1] > target:
                nums = nums[:l1]

            elif nums[l1] <= target:
                index += l1
                nums = nums[l1:]
