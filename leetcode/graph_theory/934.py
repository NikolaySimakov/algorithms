from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n=len(A)
        m=len(A[0])
        visited = set()
        q = deque()
        for i in range(n):
            if len(q) > 0:
                break
            for j in range(m):
                if A[i][j] == 1:
                    q.append((i,j))
                    break
        
        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=rr<n and 0<=cc<m and (rr,cc) not in visited and A[rr][cc]:
                    q.append((rr,cc))
                    visited.add((rr,cc))
   
        dq = deque(visited)
        ans = 0
        while dq:
            for _ in range(len(dq)):
                r,c = dq.popleft()
                for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=rr<n and 0<=cc<m and (rr,cc) not in visited:
                        if A[rr][cc] == 1:
                            return ans
                        visited.add((rr,cc))
                        dq.append((rr,cc))
            ans += 1
    

s = Solution()

# Example 1
g = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
res = s.shortestBridge(g)
print(res)

