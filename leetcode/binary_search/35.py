from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    inx = 0

    while True:
        c = len(nums)//2

        if len(nums) == 1:
            if nums[0] < target:
                inx += 1
            return inx

        if nums[c] > target:
            nums = nums[:c]

        elif nums[c] <= target:
            inx += c
            nums = nums[c:]


nums = [1, 3, 5, 6]
target = 2

res = searchInsert(
    nums,
    target
)

print(res)
