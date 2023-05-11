n = int(input())
arr = list(map(int, input().split()))

s = set()
for a in range(n - 1):
    sm = arr[a]
    if sm == 0:
        s = s | {(i, j) for i in range(a + 1) for j in range(a, n)}
    else:
        for b in range(a + 1, n):
            sm += arr[b]
            if sm == 0:
                s = s | {(i, j) for i in range(a + 1) for j in range(b, n)}
                break

if arr[n-1] == 0:
    s = s | {(i, j) for i in range(n) for j in range(n-1, n)}

print(len(s))
