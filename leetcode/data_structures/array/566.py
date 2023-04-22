from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m != r*c:
            return mat
        res = []
        cnt = 0

        for _ in range(r):
            a = []
            for _ in range(c):
                a.append(mat[(cnt)//m][(cnt) % m])
                cnt += 1
            res.append(a)

        return res


s = Solution()
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(s.matrixReshape(mat, r, c))
