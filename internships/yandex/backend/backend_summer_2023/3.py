n = int(input())
prices = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

days1 = []

mx1 = 0
for i in range(n):
    for j in range(i+1, n):
        dp[i][j] = prices[j] - prices[i]
        if dp[i][j] > mx1:
            mx1 = dp[i][j]
            days1 = [i+1, j+1]

if not days1:
    print(0)
else:

    days2 = []

    mx2 = 0
    for i in range(days1[0] + 1, n): 
        v = prices[i]
        # dp[i][j]
        for a in range(i+1, n):
            div = v/prices[a]
            for b in range(a+1, n):
                dp[a][b] = prices[b]*div - v
                if dp[a][b] > mx2:
                    mx2 = dp[a][b]
                    days1[1] = i+1
                    days2 = [a+1, b+1]
                
    if mx2 > mx1:
        print(2)
        print(*days1)
        print(*days2)
    else:
        print(1)
        print(*days1)
                