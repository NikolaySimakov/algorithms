s = input()

arr = [s[0]]
p = 1

while p <= len(s):

    c = 0
    while p + c <= len(s) and s[p:p+c] in arr:
        c += 1

    arr.append(s[p:p+c])
    p += c

arr.pop(1)
print(*arr)
