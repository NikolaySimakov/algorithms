from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(len(triangle[i])):
                prev = [j-1, j]
                mn = 10001
                for p in prev:
                    if 0 <= p < len(triangle[i-1]):
                        mn = min(mn, triangle[i-1][p])
                triangle[i][j] += mn

        return min(triangle[-1])


# Example 1
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
s = Solution()
print(s.minimumTotal(triangle))

# Example 2
triangle = [[-10]]
s = Solution()
print(s.minimumTotal(triangle))
