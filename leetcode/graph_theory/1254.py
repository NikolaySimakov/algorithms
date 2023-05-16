from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return False
            if grid[x][y] == 1:
                return True

            grid[x][y] = 1  # mark as visited
            right, left, top, bottom = dfs(
                x, y+1), dfs(x, y-1), dfs(x+1, y), dfs(x-1, y)
            return right and left and top and bottom

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1

        return count
