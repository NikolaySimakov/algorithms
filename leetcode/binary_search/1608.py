from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        n = len(nums)
        low = 0
        high = max(nums)

        def get_count(numbers, val) -> int:
            cnt = 0
            for i in numbers:
                if i >= val:
                    cnt += 1
            return cnt

        while low <= high:
            mid = low + (high - low)//2
            cnt = get_count(nums, mid)
            if cnt == mid:
                return mid
            elif cnt > mid:
                low = mid + 1
            else:
                high = mid - 1

        return -1
