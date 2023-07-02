n, m, q = map(int, input().split())
mat = []
attempts = []
res = []

for _ in range(n):
    mat.append(list(map(int, input().split())))
    
for _ in range(q):
    count = 0
    x, y, k = map(int, input().split())
    x -= 1
    y -= 1
    
    v = mat[x][y]
    
    for i in range(n):
        for j in range(m):
            if (i == x and j != y) or (i != x and j == y):
                if abs(mat[i][j] - v) <= k: count += 1
    res.append(count)
                    
    
for v in res:
    print(v)
