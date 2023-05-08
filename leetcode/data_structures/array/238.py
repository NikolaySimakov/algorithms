from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        n = len(nums)
        left = [1]*(n+1)
        right = [1]*(n+1)

        left[0] = 1
        right[n] = 1

        for i in range(1, n+1):
            left[i] = left[i-1]*nums[i-1]

        for i in range(n-1, -1, -1):
            right[i] = right[i+1]*nums[i]

        for i in range(n):
            res.append(left[i]*right[i+1])

        return res


test = Solution()

# Example 1
nums = [1, 2, 3, 4]
res = test.productExceptSelf(nums)
print(res)
