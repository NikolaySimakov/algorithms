def max_profit(prices_str: str, max_transactions: int = 4) -> int:
    # Parse the prices string to a list of integers
    prices = list(map(int, prices_str.split()))

    # If there are less than 2 prices, no transactions can be made
    if len(prices) < 2:
        return 0, []

    # Initialize a list for storing profits and transaction days
    profits = [0] * (2 * max_transactions)
    trans_days = [-1] * (2 * max_transactions)

    for i in range(1, 2 * max_transactions, 2):
        profits[i] = float('-inf')

    # Check all prices
    for i, price in enumerate(prices):
        for j in range(0, 2 * max_transactions - 1, 2):
            # Calculate max profit for buying
            if profits[j + 1] < profits[j] - price:
                profits[j + 1] = profits[j] - price
                trans_days[j + 1] = i  # Record the transaction day
            # Calculate max profit for selling
            if j + 2 < len(profits) and profits[j + 2] < profits[j + 1] + price:
                profits[j + 2] = profits[j + 1] + price
                trans_days[j + 2] = i  # Record the transaction day

    max_profit = profits[-1]
    trans_days_res = [(trans_days[i], trans_days[i + 1]) for i in range(0, len(trans_days) - 1, 2) if
                      trans_days[i] != -1 and trans_days[i + 1] != -1]

    return max_profit, trans_days_res

_ = input()
s = input()
print(max_profit(s))