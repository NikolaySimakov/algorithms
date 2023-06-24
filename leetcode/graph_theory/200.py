from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        count = 0

        def dfs(x, y):
            visited[x][y] = True
            nn = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
            for xx, yy in nn:
                if 0<=xx<n and 0<=yy<m:
                    if grid[xx][yy] == '1' and not visited[xx][yy]:
                        dfs(xx, yy)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        
        return count