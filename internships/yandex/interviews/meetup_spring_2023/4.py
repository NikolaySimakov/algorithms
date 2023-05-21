n = int(input())
p = {}
d = {}
for i in range(n):
    a, b = map(int, input().split())
    p[a] = b

arr = list(map(int, input().split()))
dif = len(arr)

for i in range(len(arr)):
    arr[i] = p[arr[i]]

    if arr[i] in d.keys():
        dif = min(dif, i - d[arr[i]])
    d[arr[i]] = i

print(dif)
