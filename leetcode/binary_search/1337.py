from typing import List


class Solution:

    # Simple solution
    # MARK: - Try another solution
    # O(N*log(N))
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat[0])

        for i in range(len(mat)):

            low = 0
            high = m - 1

            while low <= high:
                mid = (low + high)//2
                if mat[i][mid] == 1:
                    low = mid + 1
                else:
                    high = mid - 1

            mat[i] += [i, low]

        res = sorted(mat, key=lambda x: x[-1])
        return [i[-2] for i in res[:k]]


s = Solution()

# Example 1
mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
r = s.kWeakestRows(mat, k)
print(r)

# Example 2
mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
r = s.kWeakestRows(mat, k)
print(r)
