from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = dict()

        for i in range(len(arr)):
            if arr[i] - difference in dp.keys():
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1

        return max(dp.values())