N = int(input())
prices = list(map(int, input().split()))

transactions = []
max_profit = 0
sell_prices = [0] * N

sell_prices[N - 1] = prices[N - 1]
for i in range(N - 2, -1, -1):
    sell_prices[i] = max(prices[i], sell_prices[i + 1])

for i in range(N):
    if prices[i] < sell_prices[i]:
        transactions.append((i, i + 1))
        max_profit += sell_prices[i] - prices[i]

print(len(transactions))
for buy, sell in transactions:
    print(buy, sell)