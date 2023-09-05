from collections import defaultdict

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = True
flag = False
i = 0

while i < n:
    if arr1[i] != arr2[i]:
        if not flag:
            flag = True
            j = i
            
            d1 = defaultdict(int)
            d2 = defaultdict(int)
            
            while j < n and arr1[j] != arr2[j]:
                d1[arr1[j]] += 1
                d2[arr2[j]] += 1
                j += 1
                
            if d1 != d2:
                res = False
                break
        
            i = j
            
        else:
            res = False
            break
        
    i += 1

print('YES' if res else 'NO')