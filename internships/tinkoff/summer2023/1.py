a, b, c, d = list(map(int, input().split()))
print('YES' if (a <= b <= c <= d) or (a >= b >= c >= d) else 'NO')
