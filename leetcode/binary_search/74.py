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

        # n_low = 0
        # n_high = len(matrix[low]) - 1

        # while n_low < n_high:
        #     mid = n_low + (n_high - n_low)//2
        #     row = matrix[low]

        #     if row[mid] < target:
        #         n_low = mid + 1
        #     elif row[mid] > target:
        #         n_high = mid - 1

        #     print(n_low, n_high)

        # return n_low == n_high


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
