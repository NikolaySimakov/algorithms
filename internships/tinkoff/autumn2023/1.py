n, v = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for val in arr:
    if val > res and val <= v:
        res = val
        
print(res)