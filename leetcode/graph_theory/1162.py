from typing import List


##
# Solution: using BFS and queue.
# 1. Add to visited and queue all vertices that value equals to 1
# 2. Run by queue values and search nearest not visited vertices (equals to 0) and calculate distance
##

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)
        queue = []
        visited = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    visited.add((i, j))
                    queue.append((i, j, 0))

        count = 0

        while queue:
            i, j, cnt = queue.pop(0)
            count = max(cnt, count)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y, cnt+1))

        return count if count else -1
