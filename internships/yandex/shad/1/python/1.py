k, n = map(int, input().split())
c = sorted(list(map(int, input().split())))[::-1]
sm = sum(c)*(n//k)

for i in range(n % k):
    sm += c[i]

print(sm)
