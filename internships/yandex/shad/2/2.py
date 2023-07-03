n = int(input())
v = list(map(int, input().split()))
arr = [-1]*n

for i in range(n):
    arr[i-v[i]] += 1

for i in range(n-1):
    arr[i+1] += arr[i]
    arr[i] += v[i]

arr[-1] += v[-1]

print(*arr)
