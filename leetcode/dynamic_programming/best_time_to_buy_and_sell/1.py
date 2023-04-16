class Solution:

    # simple solution
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 1:
            return 0
        left = 0
        right = 1

        max_profit = max(prices[1] - prices[0], 0)

        for i in range(1, n):
            diff = prices[right] - prices[left]
            if diff > 0:
                max_profit = max(max_profit, diff)
            else:
                left = right
            right += 1

        return max_profit
