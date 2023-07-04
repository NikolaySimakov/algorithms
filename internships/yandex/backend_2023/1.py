n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = int(input())
arr3 = list(map(int, input().split()))

d = {}
for i in range(n):
    d[arr1[i]] = arr2[i]

count = 0
for i in range(1, m):
    if d[arr3[i]] != d[arr3[i-1]]:
        count += 1

print(count)

