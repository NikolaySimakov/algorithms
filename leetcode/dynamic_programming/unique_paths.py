class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v1 = arr[i-1][j] if 0 <= i-1 < m and 0 <= j < n else 0
                v2 = arr[i][j-1] if 0 <= i < m and 0 <= j-1 < n else 0
                arr[i][j] = v1 + v2

                if i == 0 and j == 0:
                    arr[0][0] = 1

        return arr[-1][-1]
