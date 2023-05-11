n, s = map(int, input().split())
arr1, arr2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)

arr1 = sorted(arr1)
arr2 = sorted(arr2)

sm = sum(arr1)

if sm < s:
    for i in range(n):
        arr1[i] += ((s-sm - 1)//n) + 1


sm = sum(arr2)

if sm > s:
    for i in range(n):
        arr2[i] -= ((sm - s - 1)//n) + 1
else:
    for i in range(n):
        arr2[i] += ((s-sm - 1)//n) + 1

print(max(arr1[n//2], arr2[n//2]))
