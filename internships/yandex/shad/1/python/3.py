n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if g[i][j] == -1:
            g[i][j] = 10**18

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = max(g[i][j], min(g[i][k], g[k][j]))


for i in range(n):
    for j in range(n):
        if i == j or g[i][j] == 10**18:
            g[i][j] = 2000000023


for i in range(n):
    print(*g[i])
