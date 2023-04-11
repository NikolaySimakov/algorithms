from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:

    def search(t):
        l = 0
        h = len(nums)

        while l <= h:
            mid = l + (h - l)//2
            if nums[mid] < t:
                l = mid + 1
            else:
                h = mid - 1

        return l

    s = search(target)
    f = search(target+1) - 1

    if nums[s] == nums[f] == target:
        return [s, f]
    return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(nums, target))
