from itertools import product

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
d = []


for _ in range(n):
    a = list(map(int, input().split()))
    a.pop(0)
    d.append(a)

c = list(map(int, input().split()))


count = float('inf')


for i in product(*d):
    ct = 0
    for j in range(len(i)):
        ct += (c[i[j]-1]/100) * arr[j]

    print(ct)
    count = min(count, ct)

print(count)
