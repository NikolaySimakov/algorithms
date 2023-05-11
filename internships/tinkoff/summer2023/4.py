# переделать


n = int(input())
arr = list(map(int, input().split()))
d = {}
mx = 1

if len(set(arr)) == 1:
    print(len(arr))
else:
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1

        d2 = {}

        for j in d.values():
            if j in d2.keys():
                d2[j] += 1
            else:
                d2[j] = 1

        ln = len(d2.keys())
        if ln == 1:
            if list(d2.values())[0] > 1:
                mx = i+1
        elif ln == 2:
            a, b = list(d2.values())
            if 1 in d2.values():
                mx = i+1

    print(mx)
