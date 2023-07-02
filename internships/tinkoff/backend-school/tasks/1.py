n = int(input())
res = [0]

ct = 1
dp = [1] + [0]*(n - 1)

for i in range(1, n):
    ct += 2
    dp[i] = dp[i-1] + ct**2
    res.append(ct**3 - dp[i])

print(*res)