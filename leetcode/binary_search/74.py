from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low < high:
            mid = low + (high - low)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                low, high = mid, mid

            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1

        if low == high:
            return target in matrix[low]
        else:
            return False


sol = Solution()

# example 1
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

solution = sol.searchMatrix(
    matrix,
    target
)
print(solution)

# example 2
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

solution = sol.searchMatrix(
    matrix,
    target
)
print(solution)
