n, x, t = map(int, input().split())
arr = list(map(int, input().split()))
# arr = [(i+1, arr[i]) for i in range(n)]
# arr.sort(key=lambda a: abs(a[1] - x))
# count = 0
# res = []

# while arr and t - abs(arr[0][1] - x) >= 0:
#     count += 1
#     index, value = arr.pop(0)
#     t -= abs(value - x)
#     res.append(index)
    
# print(count)
# if count != 0:
#     print(*res)

arr = list(enumerate(arr, 1))

def get_abs_difference(a):
    return abs(a[1] - x)

arr.sort(key=get_abs_difference)

index = 0
count = 0
res = []

while arr and index < n and t - abs(arr[index][1] - x) >= 0:
    count += 1
    t -= abs(arr[index][1] - x)
    res.append(arr[index][0])
    index += 1

print(len(res))
print(*res)