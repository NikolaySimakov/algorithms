from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        visited = [[False]*m for _ in range(n)]

        def dfs(x, y):
            cnt = 1
            visited[x][y] = True
            nn = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for xx, yy in nn:
                if 0 <= xx < n and 0 <= yy < m:
                    if grid[xx][yy] and not visited[xx][yy]:
                        cnt += dfs(xx, yy)
            return cnt

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))
        return max_area
