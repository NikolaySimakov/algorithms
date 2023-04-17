class Solution:

    # Bad solution
    def judgeSquareSum(self, c: int) -> bool:

        def is_square(n: int) -> bool:
            if n == 0:
                return True
            low = 1
            high = n - 1

            while low <= high:
                mid = low + (high - low)//2
                if mid * mid < n:
                    low = mid + 1
                elif mid * mid >= n:
                    high = mid - 1

            return low*low == n

        left = 0
        right = int(c**0.5)

        while left <= right:
            if is_square(left*left):
                if is_square(right*right):
                    total = left*left + right*right
                    if total == c:
                        return True
                    else:
                        if total > c:
                            right -= 1
                        else:
                            left += 1
                else:
                    right -= 1
            else:
                left += 1

        return False


s = Solution()

n = 1000
print(s.judgeSquareSum(n))
