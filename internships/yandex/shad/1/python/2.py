arr = []
n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))


res = 0

for i in range(n):
    for j in range(n):
        if i != j:
            for a in range(6):
                for b in range(6):
                    res += (arr[i][a] + arr[j][b])**3

print(res/(36*(n - 1)*n))
