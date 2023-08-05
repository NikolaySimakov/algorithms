s = input()

arr = []
i = 0

while i <= len(s):
    c = 0
    while s[i:i+c] in arr and i+c <= len(s):
        c += 1
    arr.append(s[i:i+c])
    i += c

arr = arr[1:-1]
print('-'.join(arr))
