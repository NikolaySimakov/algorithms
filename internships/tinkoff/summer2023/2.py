n, m, k = map(int, input().split())
minutes = 0
rem = 0

for i in range(k):
    if (n - rem) % m:
        minutes += (n - rem)//m + 1
    else:
        minutes += (n - rem)//m
    rem = minutes*m - n

print(minutes)
