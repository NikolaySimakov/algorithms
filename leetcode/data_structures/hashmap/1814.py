from typing import List


class Solution:

    def rev(self, n) -> int:
        return int(''.join(list(str(n))[::-1]))

    def countNicePairs(self, nums: List[int]) -> int:

        n = len(nums)
        d = dict()

        for i in range(n):
            v = self.rev(nums[i]) - nums[i]
            if v in d.keys():
                d[v] += 1
            else:
                d[v] = 0

        count = 0
        for i in d.values():
            count += (i + 1)*i//2

        return count % (10**9 + 7)
