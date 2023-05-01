#
# Leetcode 740. Delete and Earn
#

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(list(set(nums))) == 1:
            return sum(nums)

        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = i
            else:
                d[i] += i

        n = len(d.keys())
        keys = sorted(d.keys())
        dp = [0]*n
        dp[0] = d[keys[0]]
        dp[1] = d[keys[1]] if keys[1] - \
            keys[0] == 1 else d[keys[1]] + d[keys[0]]

        for i in range(2, n):
            if keys[i] - keys[i-1] > 1:
                dp[i] = d[keys[i]] + max(dp[i-1], dp[i-2])
            else:
                dp[i] = d[keys[i]] + max(dp[i-2], dp[i-3])

        return max(dp[-1], dp[-2])
