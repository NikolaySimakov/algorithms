from typing import List

#
# let's run through all the extreme cells
# and use dfs to remove the islands associated with them
#


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = 0
            for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= xx < n and 0 <= yy < m:
                    if grid[xx][yy] == 1:
                        dfs(xx, yy)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == n-1 or j == m-1):
                    dfs(i, j)

        return sum([sum(i) for i in grid])
