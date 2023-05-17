from typing import List


class Solution:

    # Using queue
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = []
        visited = set()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            i, j = queue.pop(0)
            for x, y in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                    mat[x][y] = mat[i][j] + 1
                    queue.append((x, y))
                    visited.add((x, y))

        return mat
