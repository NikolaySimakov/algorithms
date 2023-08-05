n = int(input())
arr = list(map(int, input().split()))

res = [0]*n

cur_indexes = [arr.index(0) + 1]

for i in range(len(cur_indexes)):
    for j in range(n):
        if arr[j] == cur_indexes[i]:
            res[j] = arr[cur_indexes[i]-1] + 1


print(*res)
