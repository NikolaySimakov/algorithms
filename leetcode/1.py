n = int(input()) + 1
arr = []

for i in range(1, n):
    ct = 0
    for j in str(i):
        ct += int(j)

    arr.append(ct)

print(max(arr))
